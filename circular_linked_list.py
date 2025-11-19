class Node:
    """Node in een circulaire enkelvoudig gelinkte lijst."""
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"


class CircularLinkedList:
    """
    Circulaire gelinkte lijst.
    Laatste node verwijst terug naar self.head.
    """
    def __init__(self):
        self.head = None

    # ----------------------------------------------------------
    # 1. APPEND: voeg element toe aan het einde van de lijst
    # ----------------------------------------------------------
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            # Eerste element in de lijst
            self.head = new_node
            new_node.next = new_node  # wijst naar zichzelf
        else:
            current = self.head

            # zoek laatste node (degene die naar head wijst)
            while current.next != self.head:
                current = current.next

            current.next = new_node   # laatste wijst nu naar nieuw
            new_node.next = self.head # nieuw wijst terug naar head

    # ----------------------------------------------------------
    # 2. PREPEND: voeg element toe aan het begin
    # ----------------------------------------------------------
    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head

            # vind laatste node (die naar head wijst)
            while current.next != self.head:
                current = current.next

            # nieuwe node wordt head
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    # ----------------------------------------------------------
    # 3. INSERT: steek element in op index
    # ----------------------------------------------------------
    def insert(self, index, value):
        if index <= 0:
            return self.prepend(value)

        new_node = Node(value)
        current = self.head
        if current is None:
            self.head = new_node
            new_node.next = new_node
            return

        pos = 0
        while pos < index - 1 and current.next != self.head:
            current = current.next
            pos += 1

        # Invoegen na "current"
        new_node.next = current.next
        current.next = new_node

    # ----------------------------------------------------------
    # 4. REMOVE: verwijder eerste node met deze waarde
    # ----------------------------------------------------------
    def remove(self, value):
        if self.head is None:
            return False

        current = self.head
        prev = None

        while True:
            if current.value == value:

                # Geval: lijst heeft maar 1 element
                if current.next == current:
                    self.head = None
                    return True

                # Geval: verwijderen van head
                if current == self.head:
                    # zoek laatste node
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next

                    # update head en tail
                    self.head = current.next
                    tail.next = self.head
                    return True

                # Geval: verwijderen van een node in het midden/einde
                prev.next = current.next
                return True

            # Volgende iteratie
            prev = current
