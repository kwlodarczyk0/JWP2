from typing import Optional
from game.board import BoardFieldStatus
from game.player import Player


class GameClass:
    """
    Class representing a Battleship game session between two players.
    Manages turns, shots, and determines the winner.
    """

    def __init__(self, p1: Player, p2: Player) -> None:
        """
        Initialize the game with two players.

        Args:
            p1 (Player): The first player.
            p2 (Player): The second player.
        """
        self.first_player: Player = p1
        self.second_player: Player = p2
        self.turn: str = p1.username
        self._winner: Optional[str] = None

    @property
    def winner(self) -> Optional[str]:
        """
        Get the username of the winner, if any.

        Returns:
            Optional[str]: The winner's username or None if no winner yet.
        """
        return self._winner

    @winner.setter
    def winner(self, value: Optional[str]) -> None:
        """
        Set the winner of the game.

        Args:
            value (Optional[str]): The winner's username or None.
        """
        self._winner = value

    def shot(self, username: str, x: int, y: int) -> None:
        """
        Process a shot from a player at the given coordinates.

        Args:
            username (str): The username of the player making the shot.
            x (int): The x-coordinate of the shot.
            y (int): The y-coordinate of the shot.

        Raises:
            Exception: If the player does not exist.
        """
        if username == self.first_player.username:
            self._make_shoot(self.first_player, self.second_player, x, y)
        elif username == self.second_player.username:
            self._make_shoot(self.second_player, self.first_player, x, y)
        else:
            raise Exception("Player does not exist")

    def _make_shoot(self, caller: Player, other: Player, x: int, y: int) -> None:
        """
        Internal method to process a shot and update boards.

        Args:
            caller (Player): The player making the shot.
            other (Player): The opponent.
            x (int): The x-coordinate of the shot.
            y (int): The y-coordinate of the shot.
        """
        if (
            self._check_user_turn(caller)
            and self.winner is None
            and self._are_coordinates_ok(x, y)
        ):
            if other.player_board.arr2[x][y] == BoardFieldStatus.OCCUPIED:
                caller.opponent_board.arr2[x][y] = BoardFieldStatus.SHIP_HIT
                other.player_board.arr2[x][y] = BoardFieldStatus.SHIP_HIT
            else:
                caller.opponent_board.arr2[x][y] = BoardFieldStatus.MISS_SHOT
                other.player_board.arr2[x][y] = BoardFieldStatus.MISS_SHOT

            self.winner = self._is_winner(other) and caller.username or None
            self.turn = other.username

    def _are_coordinates_ok(self, x: int, y: int) -> bool:
        """
        Check if the given coordinates are valid on the board.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.

        Returns:
            bool: True if coordinates are valid.

        Raises:
            Exception: If coordinates are not valid.
        """
        if 0 <= int(x) < 10 and 0 <= int(y) < 10:
            return True
        raise Exception("Coordinates are not valid")

    def _is_winner(self, player: Player) -> bool:
        """
        Check if the given player has lost (no ships left).

        Args:
            player (Player): The player to check.

        Returns:
            bool: True if the player has no ships left.
        """
        for i in range(10):
            for j in range(10):
                if player.player_board.arr2[i][j] == BoardFieldStatus.OCCUPIED:
                    return False
        return True

    def _check_user_turn(self, player: Player) -> bool:
        """
        Check if it is the given player's turn.

        Args:
            player (Player): The player to check.

        Returns:
            bool: True if it is the player's turn.
        """
        return player.username == self.turn

