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
#   Defines the tree node ADT
#
# A treenode is a simple container with three pieces of information
#   data: the contained information
#   left:  a reference to another treenode or None
#   right: a reference to another treenode or None


class Treenode(object):

    def __init__(self, data, left=None, right=None):
        """
        Create a new treenode for the given data.
        Pre-conditions:
            data:  Any data value to be stored in the treenode
            left:  Another treenode (or None, by default)
            right:  Another treenode (or None, by default)
        """
        self.__data = data
        self.__left = left
        self.__right = right
        
    def get_data(self):
        """
        Retrieve the contents of the data field.
        Return
            the data value stored previously in the node
        """
        return self.__data

    def set_data(self, val):
        """
        Set the contents of the data field to val.
        Pre-conditions:
            val:  a data value to be stored
        Post-conditions:
            stores a new data value, replacing  existing value
        Return
            None
        """
        self.__data = val

    def get_left(self):
        """
        Retrieve the contents of the left field.
        Return
            the data value stored in the left field
        """
        return self.__left

    def set_left(self, val):
        """
        Set the contents of the next field to val.
        Pre-conditions:
            val:  a Treenode, or the value None
        Post-conditions:
            stores a new next value, replacing existing value
        Return
            none
        """
        self.__left = val

    def get_right(self):
        """
        Retrieve the contents of the right field.
        Return
            the data value stored in the right field
        """
        return self.__right

    def set_right(self, val):
        """
        Set the contents of the next field to val.
        Pre-conditions:
            val:  a Treenode, or the value None
        Post-conditions:
            stores a new next value, replacing existing value
        Return
            None
        """
        self.__right = val
