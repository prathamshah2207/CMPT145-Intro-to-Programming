# Student Name: Pratham Shah                        Section Number: 01
# NSID: mvr659                                      Course Number: 41442
# Student Number: 11353450                          Instructor: Lauresa Stilling

import treenode as tn
import exampletrees
import provided_treefunctions


def subst(tnode, t, r):
    """
    Substitute a target value t with a replacement value r wherever it appears in the given tree.
    :param tnode: The root treenode
    :param t: Target value to replace
    :param r: The replacement value
    :return: None
    """

    if tnode is None:
        return None
    else:
        if tnode.get_data() == t:
            tnode.set_data(r)
        subst(tnode.get_left(), t, r)
        subst(tnode.get_right(), t, r)


def copy(tnode):
    """
    Create an exact copy of the given tree, with completely new treenodes, but exactly the same data values, in exactly the same places.
    :param tnode: The root treenode
    :return: A reference to the new tree.
    """

    if tnode is None:
        return None
    else:
        left = copy(tnode.get_left())
        right = copy(tnode.get_right())

        data = tnode.get_data()
        newtree = tn.Treenode(data)

        newtree.set_left(left)
        newtree.set_right(right)

        return newtree


def diff_sum_preorder(tnode):
    """
    Alternate between finding the difference and summation of values.
    :param tnode: The root treenode
    :return int: The result of the alternating pattern X - Y + Z based on the values encountered during the inorder traversal.

    """

    if tnode is None:
        return 0
    else:

        x = tnode.get_data()
        y = diff_sum_preorder(tnode.get_left())
        z = diff_sum_preorder(tnode.get_right())

        sum = x - y + z
        return sum


def diff_sum_inorder(tnode):
    """
    Alternate between finding the difference and summation of values.
    :param tnode: The root treenode
    :return int: The result of the alternating pattern X - Y + Z based on the values encountered during the inorder traversal.
    """

    if tnode is None:
        return

    if tnode.get_left() is not None:
        x = diff_sum_inorder(tnode.get_left())
    else:
        x = tnode.get_data()
    if tnode.get_right() is not None:
        z = diff_sum_inorder(tnode.get_right())
    else:
        z = tnode.get_data()
    y = tnode.get_data()

    return x - y + z

def diff_sum_postorder(tnode):
    """
    Alternate between finding the difference and summation of values.
    :param tnode: The root treenode
    :return int: The result of the alternating pattern X - Y + Z based on the values encountered during the inorder traversal.
    """

    if tnode is None:
        return 0

    x = tnode.get_data()
    y = diff_sum_inorder(tnode.get_right())
    z = diff_sum_inorder(tnode.get_left())

    # Alternating subtraction and addition
    if tnode.get_left() is None:
        return x - y
    elif tnode.get_right() is None:
        return x + z
    else:
        return x - y + z
