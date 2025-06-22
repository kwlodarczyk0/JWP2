import json
from enum import Enum
from typing import List


class BoardFieldStatus(Enum):
    """
    Enum representing the status of a field on the board.

    Attributes:
        FREE: The field is empty.
        OCCUPIED: The field contains part of a ship.
        SHIP_HIT: The field contains a hit ship segment.
        MISS_SHOT: The field was shot at but no ship was present.
    """

    FREE = 0
    OCCUPIED = 1
    SHIP_HIT = 2
    MISS_SHOT = 3


class Board:
    """
    Class representing the game board for Battleship.

    Attributes:
        size (int): The size of the board (default 10).
        arr2 (List[List[BoardFieldStatus]]): 2D array representing the board fields.
    """

    def __init__(self, size: int = 10) -> None:
        """
        Initialize the board with the given size and set all fields to FREE.

        Args:
            size (int): The size of the board (default 10).
        """
        self.size: int = size
        self.arr2: List[List[BoardFieldStatus]] = [
            [BoardFieldStatus.FREE for _ in range(size)] for _ in range(size)
        ]

    def __str__(self) -> str:
        """
        Return a JSON string representation of the board, with field statuses as their names.

        Returns:
            str: JSON string of the board.
        """
        serializable_board = [[cell.name for cell in row] for row in self.arr2]
        return json.dumps(serializable_board)

