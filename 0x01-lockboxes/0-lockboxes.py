#!/usr/bin/python3
"""
lockboxes
"""


def canUnlockAll(boxes):
    """
    This function returns true if all boxes can be opened else false
    """

    boxesToOpen = boxes
    keys = []
    prevKeys = []

    # stores keys of the first box
    if boxesToOpen[0]:
        box1 = boxesToOpen[0]
        for key in box1:
            keys.append(key)
        boxesToOpen[0].clear()
        boxesToOpen[0].append("opened")

    # checks if box can be opened and opens box
    for key in keys:
        for box in boxesToOpen:
            if (boxesToOpen.index(box) == key) and ("opened" not in box):
                for key in box:
                    keys.append(key)
                boxesToOpen[boxesToOpen.index(box)].clear()
                boxesToOpen[boxesToOpen.index(box)].append("opened")

    # returns true or first if all boxes can be opened or not
    boxesNotOpened = []
    for box in boxesToOpen:
        if "opened" not in box:
            boxesNotOpened.append(box)

    if boxesNotOpened == []:
        return True
    return False
