class EmptyListException(Exception):
    """Exception raised when the linked list is empty."""
    pass


class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self.head_node = None
        self.size = 0
        for value in values:
            self.push(value)

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head_node
        while current:
            yield current.value()
            current = current.next()

    def head(self):
        if not self.head_node:
            raise EmptyListException("The list is empty.")
        return self.head_node

    def push(self, value):
        new_node = Node(value)
        new_node._next = self.head_node
        self.head_node = new_node
        self.size += 1

    def pop(self):
        if not self.head_node:
            raise EmptyListException("The list is empty.")
        value = self.head_node.value()
        self.head_node = self.head_node.next()
        self.size -= 1
        return value

    def reversed(self):
        new_list = LinkedList()
        current = self.head_node
        while current:
            new_list.push(current.value())
            current = current.next()
        return new_list
