from stack import Stack

stack = None

def setup_function():
    global stack
    stack = Stack()

def test_is_empty():
    assert stack.is_empty(), "Stack should be emtpy"


def test_push():
    stack.push("first")
    stack_size = stack.size()
    assert stack_size == 1, "should have 1 element"
    stack.push("second")
    stack.push("third")
    stack_size = stack.size()
    assert stack_size == 3, "should have 3 element"


def test_pop():
    stack.push("first")
    item = stack.pop()
    assert item == 'first', "first element should be the string first"


def test_peek():
    stack.push("first")
    item = stack.peek()
    assert item == 'first', "peeked element should be the string first"
    stack_size = stack.size()
    assert stack_size == 1, "should still have 1 element"


def test_clear():
    stack.push("first")
    stack.push("second")
    stack.push("third")
    stack_size = stack.size()
    assert stack_size == 3, "should have 3 element"
    stack.clear()
    stack_size = stack.size()
    assert stack_size == 0, "should now be empty"
