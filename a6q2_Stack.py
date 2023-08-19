from a6q2_Container import Container


class Stack(Container):
    def __init__(self):
        super().__init__()
        self._top = None

    def size(self):
        return self.get_size()

    def push(self, data):
        self.push_data(data)
        self._top = self._head.get_data()

    def pop(self):
        return self.pop_data()

    def peek(self):
        return self.peek_data()
