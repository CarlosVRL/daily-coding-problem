"""
Module problem_80

Given the root of a binary tree, return a deepest node.
"""


def find_deepest(root, level, max_level, res):

    if root:
        find_deepest(root.left, ++level, max_level, res)

        if level > max_level:
            res = root.val
            max_level = level

        find_deepest(root.right, level, max_level, res)

    return res


# A Python class that represents an individual binary node in a Binary Tree
# https://www.geeksforgeeks.org/binary-tree-set-1-introduction/
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
