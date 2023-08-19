from a6q2_Container import Container
import node as N

class Queue(Container):
    def __init__(self):
        """
        Initializes a new instance of the Queue class.
        """
        super().__init__()
        self._front = None
        self._back = None

    def size(self):
        """
        Gets the size of the queue.

        Returns:
            int: The size of the queue.
        """
        return self.get_size()

    def enqueue(self, data):
        """
        Adds an element with the specified data to the back of the queue.

        Args:
            data: The data of the new element.
        """
        new_node = N.Node(data)
        if self._head is None:
            self._head = new_node
            self._front = self._head
        else:
            self._back.set_next(new_node)
        self._back = new_node
        self._size += 1

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue.

        Returns:
            The data of the element at the front of the queue, or None if the queue is empty.
        """
        if self._front is None:
            return None
        data = self._front.get_data()
        self._front = self._front.get_next()
        self._size -= 1
        if self._front is None:
            self._back = None
        return data

    def peek(self):
        """
        Returns the data of the element at the front of the queue without removing it.

        Returns:
            The data of the element at the front of the queue, or None if the queue is empty.
        """
        return self._front.get_data()
