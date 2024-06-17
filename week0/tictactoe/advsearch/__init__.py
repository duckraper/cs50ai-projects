from .alphabeta import alphabeta
from .minimax import minimax
from tictactoe import MINIMAX
from typing import Optional, Tuple, List


def best_move(
        board: List[List[Optional[str]]],
        algorithm: str
) -> Optional[Tuple[int, int]]:
    """
    De acuerdo al algoritmo elegido decide cual es la mejor jugada
    """

    return minimax(board)\
        if algorithm == MINIMAX\
        else alphabeta(board)
