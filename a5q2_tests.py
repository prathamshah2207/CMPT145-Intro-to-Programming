# Student Name: Pratham Shah                        Section Number: 01
# NSID: mvr659                                      Course Number: 41442
# Student Number: 11353450                          Instructor: Lauresa Stilling

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
reason = 'Single node tree value replaced target value'
main.subst(tnode, t, r)

if check_tree.to_string(expected_tree) != check_tree.to_string(tnode):
    print('Test2 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

# Third
test_item = 'subst()'
tnode = tn.Treenode(3, tn.Treenode(5, tn.Treenode(9, None)), tn.Treenode(10, tn.Treenode(11, None)))
t = 9
r = 0
expected_tree = tn.Treenode(3, tn.Treenode(5, tn.Treenode(0, None)), tn.Treenode(10, tn.Treenode(11, None)))
reason = 'More than one node targeted value changed'
main.subst(tnode, t, r)

if check_tree.to_string(expected_tree) != check_tree.to_string(tnode):
    print('Test3 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

# Test Case for copy(tnode) function

# First
test_item = 'copy()'
tnode = None
expected_tree = None
reason = 'Empty binary tree'
result = main.copy(tnode)

if check_tree.to_string(expected_tree) != check_tree.to_string(result):
    print('Test1 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

# Second
test_item = 'copy()'
tnode = tn.Treenode(3)
expected_tree = tn.Treenode(3)
reason = 'Tree with single node'
result = main.copy(tnode)

if check_tree.to_string(expected_tree) != check_tree.to_string(result):
    print('Test2 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

# Third
test_item = 'copy()'
tnode = tn.Treenode(3, tn.Treenode(5, tn.Treenode(9, None)), tn.Treenode(10, tn.Treenode(11, None)))
expected_tree = tn.Treenode(3, tn.Treenode(5, tn.Treenode(9, None)), tn.Treenode(10, tn.Treenode(11, None)))
reason = 'Tree with more than one node'
result = main.copy(tnode)

if check_tree.to_string(expected_tree) != check_tree.to_string(result):
    print('Test3 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

# Test Case for diff_sum_preorder(tnode)

# First
test_item = 'diff_sum_preorder()'
tnode = None
expected_tree = None
reason = 'Empty binary tree'
result = main.diff_sum_preorder(tnode)

if check_tree.to_string(expected_tree) != check_tree.to_string(tnode):
    print('Test1 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

# Second
test_item = 'diff_sum_preorder()'
tnode = tn.Treenode(3)
expected_tree = 3
reason = 'Tree with single node'
result = main.diff_sum_preorder(tnode)

if expected_tree != result:
    print('Test2 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

# Third
test_item = 'diff_sum_preorder()'
tnode = tn.Treenode(5, tn.Treenode(2, tn.Treenode(1, None, None),
                                   tn.Treenode(1, tn.Treenode(0, None, None),
                                               tn.Treenode(1, None, None))),
                    tn.Treenode(3, tn.Treenode(1, tn.Treenode(0, None, None),
                                               tn.Treenode(1, None, None)),
                                tn.Treenode(2, tn.Treenode(1, None, None),
                                            tn.Treenode(1, tn.Treenode(0, None, None),
                                                        tn.Treenode(1, None, None)))))
expected_tree = 6
reason = 'Tree with more than one node'
result = main.diff_sum_preorder(tnode)
if expected_tree != result:
    print('Test3 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

# Test Case for diff_sum_inorder(tnode) function

# First
test_item = 'diff_sum_inorder()'
tnode = None
expected_tree = 0
reason = 'Empty binary tree'
result = main.diff_sum_inorder(tnode)

if expected_tree != result:
    print('Test1 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

# Second
test_item = 'diff_sum_inorder()'
tnode = tn.Treenode(3)
expected_tree = 3
reason = 'Tree with single node'
result = main.diff_sum_inorder(tnode)

if expected_tree != result:
    print('Test2 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

# Third
test_item = 'diff_sum_inorder()'
tnode = tn.Treenode(1, tn.Treenode(3, tn.Treenode(5, tn.Treenode(9, None)), tn.Treenode(10, tn.Treenode(11, None))))
expected_tree = 17
reason = 'Tree with more than one node'
result = main.diff_sum_inorder(tnode)

if expected_tree != result:
    print('Test3 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))


# Test Case for diff_sum_postorder(tnode)

# First

test_item = 'diff_sum_postorder()'
tnode = None
expected_tree = 0
reason = 'tree with empty node'
result = main.diff_sum_postorder(tnode)

if expected_tree != result:
    print('Test1  failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

# Second

test_item = 'diff_sum_postorder()'
tnode = tn.Treenode(3)
expected_tree = 3
reason = 'tree with single node'
result = main.diff_sum_postorder(tnode)

if expected_tree != result:
    print('Test2 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

# Third

test_item = 'diff_sum_postorder()'
tnode = tn.Treenode(5, tn.Treenode(2, tn.Treenode(1, None, None),
                                   tn.Treenode(1, tn.Treenode(0, None, None),
                                               tn.Treenode(1, None, None))),
                    tn.Treenode(3, tn.Treenode(1, tn.Treenode(0, None, None),
                                               tn.Treenode(1, None, None)),
                                tn.Treenode(2, tn.Treenode(1, None, None),
                                            tn.Treenode(1, tn.Treenode(0, None, None),
                                                        tn.Treenode(1, None, None)))))
expected_tree = 8
reason = 'tree with more than one node'
result = main.diff_sum_postorder(tnode)
if expected_tree != result:
    print('Test3 failed: {}: Tree after substitution is not as expected -- {}'.format(test_item, reason))

print('*** testing complete ***')
