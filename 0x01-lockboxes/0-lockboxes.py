#!/usr/bin/python3
"""Method that determine if all boxes can be opened"""


def canUnlockAll(boxes):
    """Can unlock all boxes method"""
    keys = [0]
    for k in keys:
        for box in boxes[k]:
            if box < len(boxes):
                if box not in keys:
                    keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False
