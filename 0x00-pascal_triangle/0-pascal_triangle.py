
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
            triangle.append(newRowColomn)
        elif n > 1:
            newRowColomn = rowList * (n+1)
            colomns = len(newRowColomn)
            if newRowColomn[0] and newRowColomn[colomns - 1]:
                newRowColomn[0] = 1
                newRowColomn[colomns - 1] = 1
            else:
                for space in newRowColomn:
                    start = 0
                    if not (newRowColomn[0]) and not (newRowColomn[colomns - 1]):
                        results = prevSpace[start] + prevSpace[start + 1]
                        space = result
                    start += 1

                prevRow = newRowColomn
                triangle.append(newRowColomn)
                        
            
    return triangle
