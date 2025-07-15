# CMPT 145 Course material
# Copyright (c) 2017-2023 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#    Question nodechain_sumcountreplace starter code

# Student Name: Pratham Shah                        Section Number: 01
# NSID: mvr659                                      Course Number: 41442
# Student Number: 11353450                          Instructor: Lauresa Stilling

import node as n


def sumnc(node_chain):
    """
    Purpose:
        Given a node chain with numeric data values, calculate 
        the sum of the data values.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty, containing 
                           numeric data values
    Post-condition:
            None
    Return
            :return: the sum of the data values in the node chain
    """
    if node_chain is None:
        return 0
    else:
        walker = node_chain
        value = walker.get_data()
        return value + sumnc(walker.get_next())
    

def count_in(node_chain, value):
    """
    Purpose:
        Counts the number of times a value appears in a node chain
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
        :param value: a data value
    Return:
        :return: The number times the value appears in the node chain
    """
    counter = 0
    if node_chain is None:
        return 0
    else:
        walker = node_chain
        value_of_node = walker.get_data()
        if value_of_node == value:
            if value is None:
                value = 0
            return counter + count_in(walker.get_next(), value) + 1
        else:
            return count_in(walker.get_next(), value)


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
