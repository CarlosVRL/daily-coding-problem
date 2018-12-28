"""
Module problem_83

Invert a binary tree.
"""


def invert_binary_tree(node):

    inverted_node = Node(node.val)

    if node.right:
        inverted_node.left = invert_binary_tree(node.right)

    if node.left:
        inverted_node.right = invert_binary_tree(node.left)

    return inverted_node


# A Python class that represents an individual binary node in a Binary Tree
# https://www.geeksforgeeks.org/binary-tree-set-1-introduction/
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
