from a6q2_Container import Container

class Stack(Container):
    def __init__(self):
        """
        Initializes a new instance of the Stack class.
        """
        super().__init__()
        self._top = None

    def size(self):
        """
        Gets the size of the stack.

        Returns:
            int: The size of the stack.
        """
        return self.get_size()

    def push(self, data):
        """
        Pushes a new element with the specified data to the top of the stack.

        Args:
            data: The data of the new element.
        """
        self.push_data(data)
        self._top = self._head.get_data()

    def pop(self):
        """
        Removes and returns the top element from the stack.

        Returns:
            The data of the top element, or None if the stack is empty.
        """
        return self.pop_data()

    def peek(self):
        """
        Returns the data of the top element without removing it from the stack.

        Returns:
            The data of the top element, or None if the stack is empty.
        """
        return self.peek_data()
