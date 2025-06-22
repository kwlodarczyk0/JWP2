from typing import List
from game.board import Board


class Player:
    """
    Class representing a player in the Battleship game.

    Attributes:
        username (str): The username of the player.
        player_board (Board): The player's own board with their ships.
        opponent_board (Board): The board tracking shots at the opponent.
    """

    def __init__(self, username: str, board: List[List[object]]) -> None:
        """
        Initialize a Player with a username and a board.

        Args:
            username (str): The player's username.
            board (List[List[object]]): The initial board configuration for the player.
        """
        self.username: str = username
        self.player_board: Board = Board()
        self.opponent_board: Board = Board()
        self.player_board.arr2 = board

