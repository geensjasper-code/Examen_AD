import csv

class LinkedListNode:
    def __init__(self, task_name, duration, priority, next=None):
        self.task_name = task_name
        self.duration = duration
        self.priority = priority
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # ------------------------------
    # ADD / REMOVE / DISPLAY
    # ------------------------------
    def add_task(self, task_name, duration, priority):
        """Add a task at the end of the list"""
        new_node = LinkedListNode(task_name, duration, priority)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_task(self, task_name):
        """Remove a task by name"""
        if self.head and self.head.task_name == task_name:
            self.head = self.head.next
            return
        current = self.head
        while current and current.next and current.next.task_name != task_name:
            current = current.next
        if current and current.next:
            current.next = current.next.next
        else:
            raise ValueError(f"Task '{task_name}' not found.")

    def display_tasks(self):
        """Print all tasks in order"""
        current = self.head
        while current:
            print(f"{current.task_name} (Duration: {current.duration}, Priority: {current.priority}) -> ", end="")
            current = current.next
        print("None")

    # ------------------------------
    # SEARCH / TOTAL DURATION
    # ------------------------------
    def find_task(self, task_name):
        current = self.head
        while current:
            if current.task_name == task_name:
                return current.task_name, current.duration, current.priority
            current = current.next
        return None

    def calculate_total_duration(self):
        total = 0
        current = self.head
        while current:
            total += current.duration
            current = current.next
        return total

    # ------------------------------
    # READ TASKS FROM CSV
    # ------------------------------
    def read_tasks_from_csv(self, file_path):
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header
            for task_name, duration, priority in reader:
                self.add_task(task_name.strip(), int(duration), int(priority))

    # ------------------------------
    # HELPER METHODS FOR SORTING
    # ------------------------------
    def sorted_insert_by_priority(self, head, node):
        """Insert node into list by priority only (lowest number first)"""
        if head is None or node.priority < head.priority:
            node.next = head
            return node
        current = head
        while current.next and current.next.priority <= node.priority:
            current = current.next
        node.next = current.next
        current.next = node
        return head

    def sorted_insert_by_priority_duration(self, head, node):
        """Insert node by priority, then duration"""
        if (head is None or
            node.priority < head.priority or
            (node.priority == head.priority and node.duration < head.duration)):
            node.next = head
            return node
        current = head
        while (current.next and
               (current.next.priority < node.priority or
                (current.next.priority == node.priority and
                 current.next.duration <= node.duration))):
            current = current.next
        node.next = current.next
        current.next = node
        return head

    # ------------------------------
    # REORDER METHODS
    # ------------------------------
    def reorder_tasks_by_priority(self):
        new_head = None
        current = self.head
        while current:
            next_node = current.next
            current.next = None
            new_head = self.sorted_insert_by_priority(new_head, current)
            current = next_node
        self.head = new_head

    def reorder_tasks_by_priority_duration(self):
        new_head = None
        current = self.head
        while current:
            next_node = current.next
            current.next = None
            new_head = self.sorted_insert_by_priority_duration(new_head, current)
            current = next_node
        self.head = new_head

    # ------------------------------
    # OPTIMIZE TASK ORDER
    # ------------------------------
    def optimize_task_order(self):
        """Reorder tasks for shortest completion time:
           - Priority first (lowest number)
           - Duration next (shortest first)
        """
        self.reorder_tasks_by_priority_duration()
