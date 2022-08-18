#!/usr/bin/python3
"""
A Fuction that returns the perimeter of the island described in grid.
"""


def island_perimeter(grid):
    """
    This fuction returns the perimeter of an island described in a grid
    """

    island = grid
    land_size = 0
    perimeter = 0

    for area in island:
        for land in area:
            if land == 1:
                land_size += 1

    if land_size == 0:
        return 0
    elif land_size == 1:
        perimeter += 4
    else:
        for i in range(land_size):
            if (i == 0) or (i == (land_size - 1)):
                perimeter += 3
            else:
                perimeter += 2

    return perimeter
