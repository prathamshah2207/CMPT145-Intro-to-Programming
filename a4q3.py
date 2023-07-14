# Student Name: Pratham Shah                        Section Number: 01
# NSID: mvr659                                      Course Number: 41442
# Student Number: 11353450                          Instructor: Lauresa Stilling

import node as n
def to_string(node_chain):
    """
    Purpose:
        Create a string representation of the node chain.  E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
    Pre-conditions:
        :param node_chain:  A node-chain, possibly empty (None)
    Post-conditions:
        None
    Return: A string representation of the nodes.
    """
    if node_chain is None:
        return 'EMPTY'
    else:
        value = node_chain.get_data()
        next_node = node_chain.get_next()

        if next_node is None:
            return '[ {} | / ]'.format(str(value))
        else:
            next_str = to_string(next_node)
            return '[ {} | *-]-->{}'.format(str(value), next_str)


def copy(node_chain):
    """
    Purpose:
        Create a separate distinct copy of the node chain.
    Pre-conditions:
        :param node_chain: A node-chain, possibly empty (None)
    Post-conditions:
        A new node-chain is created with the same values and order, but it is a separate distinct chain.
    Return:
        Reference to the first node in the new chain.
    """
    if node_chain is None:
        return None

    value = node_chain.get_data()
    next_node = node_chain.get_next()

    copied_node = n.node(value)
    copied_node.set_next(copy(next_node))

    return copied_node


def replace_in(node_chain, target, replacement):
    """
    Purpose:
        Replaces each occurrence of the target value with the replacement
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
        :param target: a value that might appear in the node chain
        :param replacement: the value to replace the target
    Post-conditions:
        Each occurrence of the target value in the chain is replaced with
        the replacement value.
    Return:
        None
    """
    if node_chain is None:
        return 0
    else:
        walker = node_chain
        value = walker.get_data()
        if value == target:
            walker.set_data(replacement)
        return replace_in(walker.get_next(), target, replacement)
