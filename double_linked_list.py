class Node:
    """Een node in een dubbel gelinkte lijst."""
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"


class DoublyLinkedList:
    """Implementatie van een dubbel gelinkte lijst."""
    def __init__(self):
        self.head = None
        self.tail = None

    # ---------------------------------------
    # 1. APPEND: voeg element toe aan einde
    # ---------------------------------------
    def append(self, value):
        new_node = Node(value)

        if self.head is None:  # lijst is leeg
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node  # oude tail wijst naar nieuwe
            new_node.prev = self.tail
            self.tail = new_node       # update tail

    # ---------------------------------------
    # 2. PREPEND: voeg element toe aan begin
    # ---------------------------------------
    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:  # lijst is leeg
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # ---------------------------------------
    # 3. INSERT: steek element in op index
    # ---------------------------------------
    def insert(self, index, value):
        if index <= 0:
            return self.prepend(value)

        new_node = Node(value)
        current = self.head
        current_index = 0

        # loop tot juiste positie
        while current is not None and current_index < index:
            current = current.next
            current_index += 1

        if current is None:  # index buiten lijst → append
            return self.append(value)

        # invoegen vóór current
        previous = current.prev
        previous.next = new_node
        new_node.prev = previous
        new_node.next = current
        current.prev = new_node

    # ---------------------------------------
    # 4. REMOVE: verwijder eerste node met waarde
    # ---------------------------------------
    def remove(self, value):
        current = self.head

        while current is not None:
            if current.value == value:

                # geval: eerste node
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None  # lijst is nu leeg

                # geval: laatste node
                elif current.next is None:
                    self.tail = current.prev
                    self.tail.next = None

                # geval: tussenin
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                return True  # verwijderd

            current = current.next

        return False  # niet gevonden

    # ---------------------------------------
    # 5. FIND: zoek een waarde
    # ---------------------------------------
    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    # ---------------------------------------
    # 6. ITEREREN & PRINTEN
    # ---------------------------------------
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        return "<->".join(str(v) for v in self)
