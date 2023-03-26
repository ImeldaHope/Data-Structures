"""
Implementing a linked listbelow.
"""

class Node:
    """
    Implementing a linked listbelow.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    """
    A singly linked list data structure.

    Attributes:
        head (Node): The first node in the linked list, or None if the list is empty.
    """

    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None

    def append(self, data):
        """
        Adds a new node with the given data to the end of the linked list.

        Args:
            data: The data to store in the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def print_list(self):
        """
        Prints the data of each node in the linked list.
        """
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
