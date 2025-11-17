class DoublyLinkedList:
    class Node:
        def __init__(self, element):
            self.element = element
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def add(self, element):
        new_node = self.Node(element)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def remove(self, element):
        current = self.head

        while current is not None:
            if current.element == element:

                # Case 1: removing the head
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None

                # Case 2: removing the tail
                elif current.next is None:
                    self.tail = current.prev
                    self.tail.next = None

                # Case 3: removing from middle
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                self.length -= 1
                return True  # removed successfully

            current = current.next

        return False  # not found

    def print_forward(self):
        current = self.head
        while current:
            print(current.element, end=" <-> ")
            current = current.next
        print("None")

    def print_backward(self):
        current = self.tail
        while current:
            print(current.element, end=" <-> ")
            current = current.prev
        print("None")
