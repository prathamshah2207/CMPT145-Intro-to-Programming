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
#   Defines a few example trees

import treenode as tn


atree = tn.Treenode(2)
a = tn.Treenode(7)
b = tn.Treenode(5)
atree.set_left(a)
atree.set_right(b)
c = tn.Treenode(11)
d = tn.Treenode(6)
a.set_left(c)
a.set_right(d)

# an empty tree with a bad pun: it's empty.  Say mtree out loud.  
mtree = None

# a tree with one node only.  Yes, a bad pun too.
ctree = tn.Treenode('si')

# a larger more e-xtree-me tree
xtree = tn.Treenode(5,
              tn.Treenode(1,None,
                        tn.Treenode(4,
                                  tn.Treenode(3,tn.Treenode(2,None,None),None),
                                  None)),
              tn.Treenode(9,tn.Treenode(8,tn.Treenode(7,tn.Treenode(6,None,None),None),None),
                          tn.Treenode(1,tn.Treenode(3,None,None),tn.Treenode(3,None,None))))


# and you thought puns wouldn't get worse...
fibonatree = tn.Treenode(5,tn.Treenode(2,tn.Treenode(1,None,None),
                                     tn.Treenode(1,tn.Treenode(0,None,None),
                                                 tn.Treenode(1,None,None))),
                         tn.Treenode(3,tn.Treenode(1,tn.Treenode(0,None,None),
                                                 tn.Treenode(1,None,None)),
                                     tn.Treenode(2,tn.Treenode(1,None,None),
                                                 tn.Treenode(1,tn.Treenode(0,None,None),
                                                             tn.Treenode(1,None,None)))))


# a tree with some meaning
expr_tree = tn.Treenode('*',
                  tn.Treenode('+',
                            tn.Treenode('+',
                                      tn.Treenode(2.0, None, None),
                                      tn.Treenode(3.0, None, None)),
                            tn.Treenode(3.0, None, None)),
                  tn.Treenode('+',
                            tn.Treenode(4.0, None, None),
                            tn.Treenode('/',
                                      tn.Treenode(2.0, None, None),
                                      tn.Treenode('+',
                                                tn.Treenode(89.0, None, None),
                                                tn.Treenode(3.0, None, None)))))
