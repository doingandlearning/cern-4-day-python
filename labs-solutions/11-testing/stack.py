class Stack:
    """ A simple Stack ADT
    A stack is an ordered collection of items where
    the addition of new items and the removal of existing
    items always takes place at the same end. This end is
    commonly referred to as the 'top'. The end opposite
    the top is known as the 'base'.
    """

    def __init__(self):
        self.contents = []

    def is_empty(self):
        return self.contents == []

    def push(self, item):
        self.contents.append(item)

    def pop(self):
        return self.contents.pop()

    def peek(self):
        return self.contents[len(self.contents) - 1]

    def size(self):
        return len(self.contents)

    def clear(self):
        self.contents = []

    def __str__(self):
        return 'Stack' + str(self.contents)

    # Support the length protocol

    # Implement the iterable protocol
