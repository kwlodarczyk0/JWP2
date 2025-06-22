from typing import Any, Dict, List
from flask_socketio import SocketIO, join_room, emit
from game.board import BoardFieldStatus
import json

socketio = SocketIO()


class GameHub:
    """
    Class responsible for handling socket events and communication between clients and the game manager.
    """

    def __init__(self, config: Dict[str, Any], manager: Any) -> None:
        """
        Initialize the GameHub with configuration and a game manager.

        Args:
            config (Dict[str, Any]): Configuration dictionary.
            manager (Any): The game manager instance.
        """
        self._config = config
        self._manager = manager

    def add_player(self, data: Dict[str, Any]) -> None:
        """
        Add a player to a game group and start the game if the group is full.

        Args:
            data (Dict[str, Any]): Data containing player info and board.
        """
        username: str = data["player"]
        export_board: List[List[int]] = data["board"]
        ar = self.board(export_board)
        group = self._manager.register(username, ar)

        join_room(group.name)

        if group.full:
            emit(
                "GameStarted",
                {
                    "firstPlayer": group.game.first_player.username,
                    "secondPlayer": group.game.second_player.username,
                    "groupName": group.name,
                },
                room=group.name,
            )
            self.send_to_caller(group.game, group.game.second_player, group.name)
            self.send_to_others(group.game, group.game.first_player, group.name)
        else:
            emit("WaitingForPlayer")

    def shot(self, data: Dict[str, Any]) -> None:
        """
        Handle a shot event from a player.

        Args:
            data (Dict[str, Any]): Data containing group name, player, and coordinates.
        """
        group_name: str = data["groupName"]
        player: str = data["player"]
        x: int = data["x"]
        y: int = data["y"]

        game = self._manager.shot(group_name, player, y, x)

        if game.first_player.username == player:
            self.send_to_caller(game, game.first_player, group_name)
            self.send_to_others(game, game.second_player, group_name)
        else:
            self.send_to_caller(game, game.second_player, group_name)
            self.send_to_others(game, game.first_player, group_name)

        if game.winner is not None:
            emit("WinnerInfo", game.winner, room=group_name)
            self._manager._games.pop(group_name, None)

    def get_ships(self) -> None:
        """
        Emit the available ships configuration to the client.
        """
        with open("config/ships.json", "r") as file:
            ships = json.load(file)
            emit("Ships", ships)

    def send_message_to_group_chat(self, data: Dict[str, Any]) -> None:
        """
        Send a chat message to all players in the group.

        Args:
            data (Dict[str, Any]): Data containing group name, player, and message.
        """
        group_name: str = data["groupName"]
        player: str = data["player"]
        message: str = data["message"]
        emit("Message", {"player": player, "message": message}, room=group_name)

    def disconnect(self, data: Dict[str, Any]) -> None:
        """
        Handle a player disconnecting from the game.

        Args:
            data (Dict[str, Any]): Data containing the group name.
        """
        group_name: str = data["groupName"]
        self._manager.disconnect(group_name)
        emit("InfoAboutOpponentLeave", "You win!", room=group_name)

    # Helper functions
    def send_to_caller(self, game: Any, player: Any, group_name: str) -> None:
        """
        Send the current game status to the calling player.

        Args:
            game (Any): The game instance.
            player (Any): The player to send the status to.
            group_name (str): The group name.
        """
        from flask import request

        emit(
            "GameStatus",
            {
                "playerBoard": player.player_board.__str__(),
                "opponentBoard": player.opponent_board.__str__(),
                "turn": game.turn,
            },
            to=request.sid,
        )

    def send_to_others(self, game: Any, player: Any, group_name: str) -> None:
        """
        Send the current game status to all other players in the group.

        Args:
            game (Any): The game instance.
            player (Any): The player whose status to send.
            group_name (str): The group name.
        """
        from flask import request

        emit(
            "GameStatus",
            {
                "playerBoard": player.player_board.__str__(),
                "opponentBoard": player.opponent_board.__str__(),
                "turn": game.turn,
            },
            room=group_name,
            skip_sid=request.sid,
        )

    def board(self, json_array: List[List[int]]) -> List[List[BoardFieldStatus]]:
        """
        Convert a 2D array of integers to a 2D array of BoardFieldStatus enums.

        Args:
            json_array (List[List[int]]): The board as a 2D array of integers.

        Returns:
            List[List[BoardFieldStatus]]: The board as a 2D array of BoardFieldStatus.
        """
        arr2: List[List[BoardFieldStatus]] = [[None for _ in range(10)] for _ in range(10)]
        for i in range(10):
            for j in range(10):
                value = json_array[i][j]
                if value == 0:
                    arr2[i][j] = BoardFieldStatus.FREE
                elif value == 1:
                    arr2[i][j] = BoardFieldStatus.OCCUPIED
        return arr2

