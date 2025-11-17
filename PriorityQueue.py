class PriorityQueue:
    class Node:
        def __init__(self, element, priority):
            self.element = element
            self.priority = priority
            self.next = None

    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def enqueue(self, element, priority):
        new_node = self.Node(element, priority)

        # If queue is empty OR new node has higher priority than head
        if self.is_empty() or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            # Find the insertion point
            current = self.head
            while current.next is not None and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return None

        removed = self.head
        self.head = self.head.next
        self.length -= 1
        return removed.element

    def peek(self):
        if self.is_empty():
            return None
        return self.head.element

    def size(self):
        return self.length
