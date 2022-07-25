#!/usr/bin/python3
"""
Contains methods that find the possible solutions to the n-queens can
be placed without them attacking each other(The n-queens problem).
"""
import sys


def is_valid(board, row, col):
    """
    Checks if a position of the queen is valid
    Args:
        board: 2D array representing the board
        row: row of the queen
        col: column of the queen
    Returns:
        Boolean: True if the position is valid, False otherwise
    """
    # Check this row on left side
    if 1 in board[row]:
        return False

    upper_diag = zip(range(row, -1, -1),
                     range(col, -1, -1))
    for i, j in upper_diag:
        if board[i][j] == 1:
            return False

    lower_diag = zip(range(row, len(board), 1),
                     range(col, -1, -1))
    for i, j in lower_diag:
        if board[i][j] == 1:
            return False
