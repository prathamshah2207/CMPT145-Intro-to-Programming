# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#    Question nodechain_tostring starter code

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
    Post_conditions:
        None
    Return: A string representation of the nodes.
        NOTE: THIS VERSION OF THE FUNCTION IS KNOWN TO BE BROKEN!!!
    """
    # special case: empty node chain
    if node_chain is None:
        result = 'EMPTY'
    else:
        # walk along the chain
        walker = node_chain
        value = walker.get_data()
        # print the data
        result = '[ {} |'.format(str(value))
        while walker is not None:
            walker = walker.get_next()
            if walker is not None:
                value = walker.get_data()
            # represent the next with an arrow-like figure
                result += ' *-]-->[ {} |'.format(str(value))

        # at the end of the chain, use '/'
        result += ' / ]'

    return result

