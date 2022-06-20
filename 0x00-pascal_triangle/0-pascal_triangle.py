#!/usr/bin/python3
"""returns a pascal triangle"""


def pascal_triangle(n):
    """
    Returns a list of rows of the pascal triangke values
    """

    numberOfRows = n
    rowList = []
    triangle = []
    prevRow = []

    for n in range(numberOfRows):
        if n == 0:
            # runs for first row if triangle is one row
            rowList = [1]
            triangle.append(rowList)

        elif n == 1:
            # runs for second row or if trinlangle is two rows
            newRowColumn = rowList * (n+1)
            prevRow = newRowColumn
            triangle.append(newRowColumn)

        else:
            # runs for the rest of the rows or triangle is more than two rows
            newRowColumn = rowList * (n+1)
            columns = len(newRowColumn)

            i = 0
            start = 0
            for space in newRowColumn:

                if (i == 0) or (i == columns - 1):
                    newRowColumn[0] = 1
                    newRowColumn[columns - 1] = 1
                else:
                    input = prevRow[start] + prevRow[start + 1]
                    newRowColumn[i] = input
                    start += 1
                i += 1

            prevRow = newRowColumn
            triangle.append(newRowColumn)

    return triangle
