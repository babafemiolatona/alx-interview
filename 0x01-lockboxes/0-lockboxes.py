#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened"""
    visited = [False] * len(boxes)
    stack = [0]  # start from the first box

    while stack:
        box = stack.pop()
        visited[box] = True
        for key in boxes[box]:
            if key < len(boxes) and not visited[key]:
                stack.append(key)

    return all(visited)
