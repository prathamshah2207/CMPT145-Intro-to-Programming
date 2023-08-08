# Student Name: Pratham Shah                        Section Number: 01
# NSID: mvr659                                      Course Number: 41442
# Student Number: 11353450                          Instructor: Lauresa Stilling

from treenode import *


def ordered(tnode):
    def InterCheck(node, min_value=float('-inf'), max_value=float('inf')):
        if node is None:
            return True

        if not (min_value < node.get_data() < max_value):
            return False

        return (InterCheck(node.get_left(), min_value, node.get_data()) and
                InterCheck(node.get_right(), node.get_data(), max_value))

    return InterCheck(tnode)
