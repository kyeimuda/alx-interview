#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
"""

import copy


def rotate_2d_matrix(matrix):
    """
    2D matrix, rotate it 90 degrees clockwise function
    """

    dupMatrix = copy.deepcopy(matrix)
    lane = 0

    for row in matrix:
        index = (len(row) - 1)
        indexTo = 0

        for element in row:
            change = dupMatrix[index][lane]
            matrix[lane][indexTo] = change
            index -= 1
            indexTo += 1
        lane += 1
