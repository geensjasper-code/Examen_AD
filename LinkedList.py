class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node at the end"""
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add a node at the beginning"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_data, data):
        """Insert a node after a node with a given value"""
        current = self.head
        while current and current.data != prev_data:
            current = current.next

        if not current:
            raise ValueError("Previous node not found.")

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        """Delete the first node with the given data"""

        # If head needs to be removed
        if self.head and self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current and current.next and current.next.data != data:
            current = current.next

        if current and current.next:
            current.next = current.next.next
        else:
            raise ValueError("Value not found.")

    def print_list(self):
        """Print all elements"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

