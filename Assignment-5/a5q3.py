# Student Name: Pratham Shah                        Section Number: 01
# NSID: mvr659                                      Course Number: 41442
# Student Number: 11353450                          Instructor: Lauresa Stilling

from treenode import *


def ordered(tnode):
    """
    Check if a binary tree is ordered or not.
    This function recursively checks whether the given binary tree satisfies the ordering condition for a binary search tree, where for each node, all nodes in its left subtree have values less than the node's value, and all nodes in its right subtree have values greater than the node's value.
    :param tnode: The root node of the binary tree to be checked.
    :return bool: True if the given binary tree is ordered, False otherwise.
    """
    def InterCheck(node, min_value=float('-inf'), max_value=float('inf')):
        """
        Recursively check if a subtree satisfies the ordering condition of a Binary Tree.
        :param node: The current node being checked.
        :param min_value: The minimum allowed value for nodes in the subtree.
        :param max_value: The maximum allowed value for nodes in the subtree.
        :return bool: True if the subtree rooted at 'node' is ordered, False otherwise.
        """
        if node is None:
            return True

        if not (min_value < node.get_data() < max_value):
            return False

        return (InterCheck(node.get_left(), min_value, node.get_data()) and
                InterCheck(node.get_right(), node.get_data(), max_value))

    return InterCheck(tnode)
