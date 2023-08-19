from a6q2_Container import Container


class Stack(Container):
    def __init__(self):
        super().__init__()

    def size(self):
        return self.get_size()

    def push(self, data):
        self.push_data(data)

    def pop(self):
        return self.pop_data()

    def peek(self):
        return self.peek_data()
