class Node:
    """Node used in the linked stack: stores a value and a pointer to the next node."""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value})"


class LinkedStack:
    """A stack implemented using a singly linked list.
       The top of the stack is the head of the list.
    """

    def __init__(self):
        self.top = None
        self._size = 0   # keep track of number of elements

    # -------------------------------------------------------
    # 1. PUSH: place a new element on top of the stack
    # -------------------------------------------------------
    def push(self, value):
        new_node = Node(value, next=self.top)
        self.top = new_node
        self._size += 1

    # -------------------------------------------------------
    # 2. POP: remove and return top element
    # -------------------------------------------------------
    def pop(self):
        if self.top is None:
            raise IndexError("Pop from empty stack")

        value = self.top.value
        self.top = self.top.next
        self._size -= 1
        return value

    # -------------------------------------------------------
    # 3. PEEK: return top element without removing it
    # -------------------------------------------------------
    def peek(self):
        if self.top is None:
            return None
        return self.top.value

    # -------------------------------------------------------
    # 4. IS_EMPTY: return True if stack has no elements
    # -------------------------------------------------------
    def is_empty(self):
        return self.top is None

    # -------------------------------------------------------
    # 5. SIZE: number of elements in the stack
    # -------------------------------------------------------
    def size(self):
        return self._size

    # -------------------------------------------------------
    # 6. CLEAR: remove all elements
    # -------------------------------------------------------
    def clear(self):
        self.top = None
        self._size = 0

    # -------------------------------------------------------
    # 7. ITERATION & STRING REPRESENTATION
    # -------------------------------------------------------
    def __iter__(self):
        """Iterate from top to bottom."""
        current = self.top
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        return "TOP -> " + " -> ".join(str(v) for v in self) + " -> None"
