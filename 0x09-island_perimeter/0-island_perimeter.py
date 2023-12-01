#!/usr/bin/python3
"""
A Fuction that returns the perimeter of the island described in grid.
"""


def island_perimeter(grid):
    """
    This fuction returns the perimeter of an island described in a grid
    """

    m = len(grid)
    n = len(grid[0])
    land = 0
    nei=0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                land+=1
                if i < m-1 and grid[i+1][j]==1:
                    nei+=1
                if j < n-1 and grid[i][j+1]==1:
                    nei+=1
    return land*4-2*nei

