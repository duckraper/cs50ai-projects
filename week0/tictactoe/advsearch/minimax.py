from typing import Optional, Set, Tuple, List
from tictactoe import (
    terminal,
    player,
    utility,
    result,
    actions,
    X
)


def minimax(board: List[List[Optional[str]]]) -> Optional[Tuple[int, int]]:
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    p: str = player(board)
    avaiable_actions: Set[Tuple[int, int]] = actions(board)
    move: Tuple[int, int]

    if p == X:
        value: int = -float('inf')
        for action in avaiable_actions:
            new_value: int = min_value(result(board, action))
            if new_value > value:
                value = new_value
                move = action

    else:
        value: int = float('inf')
        for action in avaiable_actions:
            new_value: int = max_value(result(board, action))
            if new_value < value:
                value = new_value
                move = action

    return move


def max_value(board: List[List[Optional[str]]]) -> int:
    if terminal(board):
        return utility(board)

    value: int = -float('inf')

    for action in actions(board):
        value = max(value, min_value(result(board, action)))

    return value


def min_value(board: List[List[Optional[str]]]) -> int:
    if terminal(board):
        return utility(board)

    value: int = float('inf')

    for action in actions(board):
        value = min(value, max_value(result(board, action)))

    return value
