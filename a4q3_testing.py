import a4q3 as func_file
import node as n


### Test cases for to_string() function

test_item = 'to_string()'
data_in = None
expected = 'EMPTY'
reason = 'Empty node chain'
result = func_file.to_string(data_in)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


data_in = n.node(1)
expected = '[ 1 | / ]'
reason = 'node chain with one node'
result = func_file.to_string(data_in)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


data_in = n.node(1, n.node('two', n.node(3)))
expected = '[ 1 | *-]-->[ two | *-]-->[ 3 | / ]'
reason = 'node chain with three nodes'
result = func_file.to_string(data_in)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


### Test cases for copy() function

test_item = 'copy()'
data_in = None
expected = None
reason = 'Empty node chain'
result = func_file.copy(data_in)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


data_in = n.node(1)
expected = '[ 1 | / ]'
reason = 'node chain with one node'
result = func_file.to_string(func_file.copy(data_in))
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


data_in = n.node(1, n.node('two', n.node(3)))
expected = '[ 1 | *-]-->[ two | *-]-->[ 3 | / ]'
reason = 'node chain with three nodes'
result = func_file.to_string(func_file.copy(data_in))
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


### Test cases for replace_in() function

test_item = "replace_in()"

chain_in = None
target_in = 1
repl_in = 0
expected_str = "EMPTY"
reason = 'empty node chain'
func_file.replace_in(chain_in, target_in, repl_in)
result_str = func_file.to_string(chain_in)
if result_str != expected_str:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result_str, expected_str, reason))


chain_in = n.node(1, n.node(2))
target_in = 0
repl_in = 1
expected_str = "[ 1 | *-]-->[ 2 | / ]"
reason = 'node chain with two nodes, target not present'
func_file.replace_in(chain_in, target_in, repl_in)
result_str = func_file.to_string(chain_in)
if result_str != expected_str:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result_str, expected_str, reason))


chain_in = n.node(1, n.node(2, n.node(3, n.node(1, n.node(4)))))
target_in = 1
repl_in = 10
expected_str = "[ 10 | *-]-->[ 2 | *-]-->[ 3 | *-]-->[ 10 | *-]-->[ 4 | / ]"
reason = 'node chain with multiple nodes, target present multiple times'
func_file.replace_in(chain_in, target_in, repl_in)
result_str = func_file.to_string(chain_in)
if result_str != expected_str:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result_str, expected_str, reason))

print('*** testing complete ***')
