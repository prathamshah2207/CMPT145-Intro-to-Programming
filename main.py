import node as N  # Import the Node class as N from your node file

class Container:
    def __init__(self, size):
        self.size = size
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return self.size == self.size()

    def push(self, data):
        if not self.is_full():
            new_node = N.Node(data)
            new_node.set_next(self.top)
            self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped_data = self.top.get_data()
            self.top = self.top.get_next()
            return popped_data

    def peek(self):
        if not self.is_empty():
            return self.top.get_data()
