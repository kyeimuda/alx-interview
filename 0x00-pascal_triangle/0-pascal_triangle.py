#!/usr/bin/python3
"""returns a pascal triangle"""

def pascal_triangle(n):
    """
    Returns a list of rows of the pascal triangke values
    """

    numberOfRows = n
    rowList = []

    for n in range(numberOfRows):
        new = str(11 ** n)

        rowList.append(new)

        return rowList
