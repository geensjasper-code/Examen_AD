from typing import Any, Iterator, Optional


class Node:
    """Internal node for the LinkedList."""
    __slots__ = ("element", "next")

    def __init__(self, element: Any, next: Optional["Node"] = None) -> None:
        self.element = element
        self.next: Optional[Node] = next


class LinkedList:
    # ------------------------------------------------------------------
    # Fields
    # ------------------------------------------------------------------
    def __init__(self) -> None:
        """Creates an empty linked list."""
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size: int = 0

    # ------------------------------------------------------------------
    # Basic add / get / remove at ends
    # ------------------------------------------------------------------
    def addFirst(self, e: Any) -> None:
        """Adds a new element to the head of the list."""
        new_node = Node(e, self._head)
        self._head = new_node
        if self._tail is None:            # list was empty
            self._tail = new_node
        self._size += 1

    def addLast(self, e: Any) -> None:
        """Adds a new element to the tail of the list."""
        new_node = Node(e, None)
        if self._tail is None:            # list was empty
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def getFirst(self) -> Any:
        """Returns the first element in the list (or None if empty)."""
        return None if self._head is None else self._head.element

    def getLast(self) -> Any:
        """Returns the last element in the list (or None if empty)."""
        return None if self._tail is None else self._tail.element

    def removeFirst(self) -> Any:
        """Removes the first element from the list and returns it."""
        if self._head is None:
            return None
        temp = self._head
        self._head = self._head.next
        self._size -= 1
        if self._head is None:            # list became empty
            self._tail = None
        return temp.element

    def removeLast(self) -> Any:
        """Removes the last element from the list and returns it."""
        if self._head is None:
            return None
        if self._head is self._tail:      # only one element
            temp = self._head
            self._head = self._tail = None
            self._size = 0
            return temp.element

        # more than one element – walk to second-last
        prev = self._head
        while prev.next is not self._tail:
            prev = prev.next
        temp = self._tail
        prev.next = None
        self._tail = prev
        self._size -= 1
        return temp.element

    # ------------------------------------------------------------------
    # Convenience add / insert
    # ------------------------------------------------------------------
    def add(self, e: Any) -> None:
        """Same as addLast(e)."""
        self.addLast(e)

    def insert(self, index: int, e: Any) -> None:
        """
        Adds a new element at the specified index.
        If index <= 0  -> insert at the front.
        If index >= size -> insert at the end.
        """
        if index <= 0:
            self.addFirst(e)
        elif index >= self._size:
            self.addLast(e)
        else:
            prev = self._head
            for _ in range(index - 1):
                prev = prev.next
            new_node = Node(e, prev.next)
            prev.next = new_node
            self._size += 1

    # ------------------------------------------------------------------
    # Clear / size / emptiness
    # ------------------------------------------------------------------
    def clear(self) -> None:
        """Removes all the elements from this list."""
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self) -> bool:
        """Returns true if this list contains no elements."""
        return self._size == 0

    def getSize(self) -> int:
        """Returns the number of elements in this list."""
        return self._size

    # ------------------------------------------------------------------
    # Search / membership
    # ------------------------------------------------------------------
    def contains(self, e: Any) -> bool:
        """Returns true if this list contains the element."""
        return self.indexOf(e) != -1

    def get(self, index: int) -> Any:
        """Returns the element at the specified index."""
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        current = self._head
        for _ in range(index):
            current = current.next
        return current.element

    def indexOf(self, e: Any) -> int:
        """Returns the index of the first matching element, or -1."""
        index = 0
        current = self._head
        while current is not None:
            if current.element == e:
                return index
            current = current.next
            index += 1
        return -1

    def lastIndexOf(self, e: Any) -> int:
        """Returns the index of the last matching element, or -1."""
        index = 0
        last = -1
        current = self._head
        while current is not None:
            if current.element == e:
                last = index
            current = current.next
            index += 1
        return last

    # ------------------------------------------------------------------
    # Removal by element / by index
    # ------------------------------------------------------------------
    def remove(self, e: Any) -> bool:
        """
        Removes the first occurrence of e from this list.
        Returns True if an element was removed, False otherwise.
        """
        if self._head is None:
            return False

        # special case: first element
        if self._head.element == e:
            self.removeFirst()
            return True

        prev = self._head
        current = self._head.next
        while current is not None:
            if current.element == e:
                prev.next = current.next
                if current is self._tail:
                    self._tail = prev
                self._size -= 1
                return True
            prev, current = current, current.next
        return False

    def removeAt(self, index: int) -> Any:
        """Removes the element at the specified index and returns it."""
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        if index == 0:
            return self.removeFirst()
        if index == self._size - 1:
            return self.removeLast()

        prev = self._head
        for _ in range(index - 1):
            prev = prev.next
        current = prev.next
        prev.next = current.next
        self._size -= 1
        return current.element

    # ------------------------------------------------------------------
    # Update
    # ------------------------------------------------------------------
    def set(self, index: int, e: Any) -> Any:
        """
        Sets the element at the specified index and returns the element
        that was previously at that index.
        """
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        current = self._head
        for _ in range(index):
            current = current.next
        old = current.element
        current.element = e
        return old

    # ------------------------------------------------------------------
    # Iteration support
    # ------------------------------------------------------------------
    def __iter__(self) -> Iterator[Any]:
        """Returns an iterator for this linked list."""
        current = self._head
        while current is not None:
            yield current.element
            current = current.next