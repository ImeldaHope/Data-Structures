"""
Implementing a queue using linked list
"""
class Node:
    """
    Implementing a queue using linked list
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    """A Queue data structure implemented using a singly linked list.

    A Queue is a First-In, First-Out (FIFO) data structure where elements are
    inserted at the back and removed from the front.

    Attributes:
        head (Node): A reference to the first node in the queue.
        tail (Node): A reference to the last node in the queue.
        size (int): The number of elements in the queue.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        """
        Implementing a queue using linked list
        """
        return self.size == 0

    def enqueue(self, data):
        """
        Implementing a queue using linked list
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        """
        Implementing a queue using linked list
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return data

    def peek(self):
        """
        Implementing a queue using linked list
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.head.data

    def __len__(self):
        return self.size
