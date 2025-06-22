import threading
from typing import Dict, Optional, Any
from game.game_group import GameGroup


class GameManager:
    """
    Class responsible for managing all Battleship games and player registrations.
    """

    def __init__(self) -> None:
        """
        Initialize the GameManager with empty games and a lock for thread safety.
        """
        self._games: Dict[str, GameGroup] = {}
        self._waiting_group: Optional[GameGroup] = None
        self._lock: threading.Lock = threading.Lock()

    def register(self, name: str, export_board: Any) -> GameGroup:
        """
        Register a player and assign them to a game group.

        Args:
            name (str): The player's username.
            export_board (Any): The player's board configuration.

        Returns:
            GameGroup: The group the player was assigned to.
        """
        with self._lock:
            if self._waiting_group is None:
                self._waiting_group = GameGroup()
                self._games[self._waiting_group.name] = self._waiting_group

            self._waiting_group.add_player(name, export_board)
            ret_val = self._waiting_group

            if self._waiting_group.full:
                self._waiting_group = None

            return ret_val

    def shot(self, group_name: str, player: str, x: int, y: int) -> Any:
        """
        Process a shot for a given group and player.

        Args:
            group_name (str): The name of the game group.
            player (str): The player's username.
            x (int): The x-coordinate of the shot.
            y (int): The y-coordinate of the shot.

        Returns:
            Any: The updated game instance.

        Raises:
            Exception: If the game is not created.
        """
        with self._lock:
            try:
                game = self._games[group_name].game
                game.shot(player, int(x), int(y))
                return game
            except Exception:
                raise Exception("GAME NOT CREATED")

    def disconnect(self, group_name: str) -> None:
        """
        Remove a game group when a player disconnects.

        Args:
            group_name (str): The name of the group to remove.
        """
        with self._lock:
            if group_name in self._games:
                del self._games[group_name]

