import node as N


class Container:
    def __init__(self):
        self.__size = 0
        self.__head = None

    def is_empty(self):
        return self.__size == 0

    def get_size(self):
        return self.__size

    def push_data(self, value):
        new_node = N.Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            new_node.set_next(self.__head)
            self.__head = new_node
        self.__size += 1

    def pop_data(self):
        if self.__head is None:
            return None
        data = self.__head.get_data()
        self.__head = self.__head.get_next()
        self.__size -= 1
        return data

    def peek_data(self):
        return self.__head.get_data()
