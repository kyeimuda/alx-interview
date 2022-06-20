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
            rowList = [1]
            triangle.append(rowList)
            
        elif n == 1:
            newRowColomn = rowList * (n+1)
            prevRow = newRowColomn
            print(prevRow)
            triangle.append(newRowColomn)

        else:
            print("===================")
            newRowColomn = rowList * (n+1)
            colomns = len(newRowColomn)

            i = 0
            start = 0
            for space in newRowColomn:
                
                if (i == 0) or (i == colomns - 1):
                    newRowColomn[0] = 1
                    newRowColomn[colomns - 1] = 1
                else:
                    input = prevRow[start] + prevRow[start + 1]
                    newRowColomn[i] = input
                    start += 1
                i += 1

            prevRow = newRowColomn
            triangle.append(newRowColomn)
            
                
    return triangle
