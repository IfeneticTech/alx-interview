#!/usr/bin/python3
"""Solves the lock boxes puzzle"""


def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes (list): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    if len(boxes) <= 1:
        return True

    opened = [False] * len(boxes)
    opened[0] = True
    keys = set(boxes[0])

    while keys:
        new_keys = set()
        for key in keys:
            if key < len(boxes) and not opened[key]:
                opened[key] = True
                new_keys.update(boxes[key])
        if not new_keys:
            break
        keys = new_keys

    return all(opened)


def main():
    """Entry point"""
    boxes = [
        [1],          # Box 0 has a key to box 1
        [2],          # Box 1 has a key to box 2
        [3],          # Box 2 has a key to box 3
        []            # Box 3 has no keys
    ]
    print(canUnlockAll(boxes))  # Should print True


if __name__ == '__main__':
    main()
