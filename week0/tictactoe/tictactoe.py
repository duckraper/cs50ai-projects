"""
Tic Tac Toe Player
"""

from copy import deepcopy
from typing import Optional, Set, Tuple, List
import math

X: str = "X"
O: str = "O"
EMPTY = None
MINIMAX = "minimax"
ALPHABETA = "alphabeta"


count:int = 0

def initial_state() -> List[List[Optional[str]]]:
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board: List[List[Optional[str]]]) -> str:
    """
    Returns player who has the next turn on a board.
    """
    count_X: int = sum(tile != EMPTY for row in board for tile in row)

    return X if count_X % 2 == 0 else O


def actions(board: List[List[Optional[str]]]) -> Set[Tuple[int, int]]:
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    a: Set[Tuple[int, int]] = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                a.add((i, j))

    return a


def result(board: List[List[Optional[str]]], action: Tuple[int, int]) -> List[List[Optional[str]]]:
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    relative_board = deepcopy(board)

    # validar que sea una accion valida
    if relative_board[i][j] is not EMPTY:
        raise Exception("La accion no es una accion valida.")

    relative_board[i][j] = player(relative_board)
    global count
    count += 1
    return relative_board


def winner(board: List[List[Optional[str]]]) -> Optional[str]:
    """
    Returns the winner of the game, if there is one.
    """
    for symbol in (X, O):
        if any(all(board[i][j] == symbol for i in range(3)) for j in range(3)):
            return symbol

        if any(all(tile == symbol for tile in board[i]) for i in range(3)):
            return symbol

        if all(board[i][i] == symbol for i in range(3)) or \
                all(board[i][2 - i] == symbol for i in range(3)):
            return symbol

    if any(board[i][j] is EMPTY for i in range(3) for j in range(3)):
        return None

    return None


def terminal(board: List[List[Optional[str]]]) -> bool:
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    # comprueba si hay espacios vacíos
    if any(board[i][j] is EMPTY for i in range(3) for j in range(3)):
        return False

    return True


def utility(board: List[List[Optional[str]]]) -> int:
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    w: str = winner(board)
    u: int = 0

    if w == X:
        u = 1
    elif w == O:
        u = -1

    return u
