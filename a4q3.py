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
