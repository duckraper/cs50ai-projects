from typing import Optional, Set, Tuple, List
from tictactoe import (
    terminal,
    player,
    utility,
    result,
    actions,
    X
)


def alphabeta(
        board: List[List[Optional[str]]],
        alpha: int = -float('inf'),
        beta: int = float('inf')
) -> Optional[Tuple[int, int]]:
    """
    Retorna el movimiento mas optimo usando alpha-beta pruning
    """
    if terminal(board):
        return None

    p: str = player(board)
    avaiable_actions: Set[Tuple[int, int]] = actions(board)
    move: Tuple[int, int]

    if p == X:
        value: int = -float('inf')
        for action in avaiable_actions:
            new_value: int = min_value(result(board, action), alpha, beta)
            if new_value > value:
                value = new_value
                move = action
            alpha = max(alpha, value)
            if alpha >= beta:
                break

    else:
        value: int = float('inf')
        for action in avaiable_actions:
            new_value: int = max_value(result(board, action), alpha, beta)
            if new_value < value:
                value = new_value
                move = action
            beta = min(beta, value)
            if alpha >= beta:
                break

    return move


def max_value(board: List[List[Optional[str]]], alpha: int, beta: int) -> int:
    if terminal(board):
        return utility(board)

    value: int = -float('inf')

    for action in actions(board):
        value = max(value, min_value(result(board, action), alpha, beta))
        alpha = max(alpha, value)
        if alpha >= beta:
            break

    return value


def min_value(board: List[List[Optional[str]]], alpha: int, beta: int) -> int:
    if terminal(board):
        return utility(board)

    value: int = float('inf')

    for action in actions(board):
        value = min(value, max_value(result(board, action), alpha, beta))
        beta = min(beta, value)
        if alpha >= beta:
            break

    return value
