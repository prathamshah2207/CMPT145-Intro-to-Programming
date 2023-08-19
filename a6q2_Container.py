import node as N

class Container:
    def __init__(self):
        """
        Initializes a new instance of the Container class.
        """
        self._size = 0
        self._head = None

    def is_empty(self):
        """
        Checks if the container is empty.

        Returns:
            bool: True if the container is empty, False otherwise.
        """
        return self._size == 0

    def get_size(self):
        """
        Gets the size of the container.

        Returns:
            int: The size of the container.
        """
        return self._size

    def push_data(self, value):
        """
        Pushes a new element with the specified value to the top of the container.

        Args:
            value: The value of the new element.
        """
        new_node = N.Node(value)
        if self._head is None:
            self._head = new_node
        else:
            new_node.set_next(self._head)
            self._head = new_node
        self._size += 1

    def pop_data(self):
        """
        Removes and returns the top element from the container.

        Returns:
            The value of the top element, or None if the container is empty.
        """
        if self._head is None:
            return None
        data = self._head.get_data()
        self._head = self._head.get_next()
        self._size -= 1
        return data

    def peek_data(self):
        """
        Returns the value of the top element without removing it from the container.

        Returns:
            The value of the top element, or None if the container is empty.
        """
        if self._head is None:
            return None
        return self._head.get_data()
