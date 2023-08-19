import node as N


class Container:
    def __init__(self):
        self._size = 0
        self._head = None

    def is_empty(self):
        return self._size == 0

    def get_size(self):
        return self._size

    def push_data(self, value):
        new_node = N.Node(value)
        if self._head is None:
            self._head = new_node
        else:
            new_node.set_next(self._head)
            self._head = new_node
        self._size += 1

    def pop_data(self):
        if self._head is None:
            return None
        data = self._head.get_data()
        self._head = self._head.get_next()
        self._size -= 1
        return data

    def peek_data(self):
        return self._head.get_data()
