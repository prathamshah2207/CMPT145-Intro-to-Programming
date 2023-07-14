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
