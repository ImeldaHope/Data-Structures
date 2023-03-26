"""
implementation of a queue that would have an average performance of O(1) for
enqueue and dequeue operations.
"""
class CircularQueue:
    """A Queue data structure implemented using a circular buffer.

    A CircularQueue is a First-In, First-Out (FIFO) data structure where elements are
    inserted at the back and removed from the front.

    Attributes:
        buffer (list): A list that represents the circular buffer.
        head (int): An index that points to the front of the queue.
        tail (int): An index that points to the back of the queue.
        size (int): The number of elements in the queue.
        capacity (int): The maximum number of elements the queue can hold.
    """

    def __init__(self, capacity):
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = capacity

    def is_empty(self):
        """Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.size == 0

    def is_full(self):
        """Check if the queue is full.

        Returns:
            bool: True if the queue is full, False otherwise.
        """
        return self.size == self.capacity

    def enqueue(self, data):
        """Add an element to the back of the queue.

        Args:
            data: The data to be added to the queue.

        Raises:
            IndexError: If the queue is full.
        """
        if self.is_full():
            raise IndexError("Queue is full")
        self.buffer[self.tail] = data
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        """Remove and return the element at the front of the queue.

        Returns:
            The element at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        data = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return data

    def peek(self):
        """Return the element at the front of the queue without removing it.

        Returns:
            The element at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.buffer[self.head]

    def __len__(self):
        """Return the number of elements in the queue.

        Returns:
            The number of elements in the queue.
        """
        return self.size
