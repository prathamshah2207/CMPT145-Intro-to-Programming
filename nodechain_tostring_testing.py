# CMPT 145:Question nodechain_tostring tests code
# test script

# import nodechain_tostring_provided as to_string_file
import a3q2 as to_string_file
import node as n

#### UNIT TEST CASES
test_item = 'to_string()'
data_in = None
expected = 'EMPTY'
reason = 'Empty node chain'

result = to_string_file.to_string(data_in)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


data_in = n.Node(1)
expected = '[ 1 | / ]'
reason = 'node chain with one node'

result = to_string_file.to_string(data_in)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


data_in = n.Node(1, n.Node('two'))
expected = '[ 1 | *-]-->[ two | / ]'
reason = 'node chain with two nodes'

result = to_string_file.to_string(data_in)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))


data_in = n.Node(1, n.Node('two', n.Node(3)))
expected = '[ 1 | *-]-->[ two | *-]-->[ 3 | / ]'
reason = 'node chain with three nodes'

result = to_string_file.to_string(data_in)
if result != expected:
    print('Test failed: {}: got "{}" expected "{}" -- {}'.format(test_item, result, expected, reason))

print('*** testing complete ***')
