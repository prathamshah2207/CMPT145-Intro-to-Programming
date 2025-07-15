import a6q2_Stack as Stack
def test_4():
    test_objective = 'size()'
    reason = 'stack with one value'
    astack = Stack.Stack()
    result = astack.peek()
    expected = None
    if result != expected:
        print("fail")
    else:
        print("pass")