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

    
    if boxes[0]:
        box1 = boxes[0]
        for key in box1:
            keys.append(key)
            boxes[0] = "opened"

            
    for box in boxes:
        if (len(box) != 0) and (box != boxes[0]):
            for key in box:
                keys.append(key)
    finalkeys = set(keys)
    index = 0
    for key in finalkeys:
        for box in boxes:
            if box == boxes[0]:
                index += 1
            else:
                if key == index:
                    box = "opened"
                    index += 1

                
    for box in boxes:
        if box != "opened":
            return False
        return True
