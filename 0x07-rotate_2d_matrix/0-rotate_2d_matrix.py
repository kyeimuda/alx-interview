#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """
    2D matrix, rotate it 90 degrees clockwise function
    """
    rows = len(matrix[0])

    dupmatrix = [[row[i] for row in matrix] for i in range(rows)]

    matrix.clear()

    for row in dupmatrix:
        row.reverse()

    for row in dupmatrix:
        matrix.append(row)
