import uuid
from typing import Optional
from game.game_class import GameClass
from game.player import Player


class GameGroup:
    """
    Class representing a group for a Battleship game, containing two players and the game instance.
    """

    def __init__(self) -> None:
        """
        Initialize an empty game group with a unique name.
        """
        self._player1: Optional[Player] = None
        self._player2: Optional[Player] = None
        self._game: Optional[GameClass] = None
        self.name: str = str(uuid.uuid4())

    @property
    def game(self) -> GameClass:
        """
        Get the game instance for this group.

        Returns:
            GameClass: The game instance.

        Raises:
            ValueError: If the game has not been created yet.
        """
        if self._game is None:
            raise ValueError("Game not created")
        return self._game

    @property
    def full(self) -> bool:
        """
        Check if the group is full (has two players and a game created).

        Returns:
            bool: True if the group is full.
        """
        return self._game is not None

    def add_player(self, name: str, export_board: list) -> None:
        """
        Add a player to the group. When the second player is added, the game is created.

        Args:
            name (str): The player's username.
            export_board (list): The player's board configuration.
        """
        if self._player1 is None:
            self._player1 = Player(name, export_board)
        else:
            self._player2 = Player(name, export_board)
            self._game = GameClass(self._player1, self._player2)

