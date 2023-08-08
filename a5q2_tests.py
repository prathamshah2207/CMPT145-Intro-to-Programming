# Student Name: Pratham Shah                        Section Number: 01
# NSID: mvr659                                      Course Number: 41442
# Student Number: 11353450                          Instructor: Lauresa Stilling

import exampletrees as et
import treenode as tn
import a5q2 as main
import provided_treefunctions as check_tree

# Test Case for subst(tnode, t, r) function

# First
test_item = 'subst()'
tnode = None
t = 5
r = 999
expected_tree = None
reason = 'Empty binary tree'
result = main.subst(tnode, t, r)

if check_tree.to_string(expected_tree) != check_tree.to_string(result):
    print('Test1 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

# Second
test_item = 'subst()'
tnode = tn.Treenode(3)
t = 3
r = 2
expected_tree = tn.Treenode(2)
reason = 'Empty binary tree'
main.subst(tnode, t, r)

if check_tree.to_string(expected_tree) != check_tree.to_string(tnode):
    print('Test2 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

# Third
test_item = 'subst()'
tnode = tn.Treenode(3, tn.Treenode(5, tn.Treenode(9, None)), tn.Treenode(10, tn.Treenode(11, None)))
t = 9
r = 0
expected_tree = tn.Treenode(3, tn.Treenode(5, tn.Treenode(0, None)), tn.Treenode(10, tn.Treenode(11, None)))
reason = 'Empty binary tree'
main.subst(tnode, t, r)

if check_tree.to_string(expected_tree) != check_tree.to_string(tnode):
    print('Test3 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

print('*** testing complete ***')
