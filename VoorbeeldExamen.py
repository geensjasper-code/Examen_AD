
class LinkedListNode:
    def __init__(self, task_name, duration, priority, next = None):
        self.task_name = task_name
        self.duration = duration
        self.priority = priority
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_task(self, task_name, duration, priority):
        new_node = LinkedListNode(task_name, duration, priority)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_task(self, task_name):
        """Delete the first node with the given task_name"""

        # If head needs to be removed
        if self.head and self.head.task_name == task_name:
            self.head = self.head.next
            return

        current = self.head
        while current and current.next and current.next.data != task_name:
            current = current.next

        if current and current.next:
            current.next = current.next.next
        else:
            raise ValueError("Value not found.")

    def display_tasks(self):
        """Print all elements"""
        current = self.head
        while current:  # == while current is not None:
            print(current.task_name, end=" -> ")
            current = current.next
        print("None")

    def find_task(self, task_name):
        current = self.head
        while current:
            if current.task_name == task_name:
                return current.task_name, current.duration, current.priority
            current = current.next

    def calculate_total_duration(self):
        current = self.head
        total_duration = 0
        while current:
            total_duration += current.duration
            current = current.next
        return total_duration


    def read_tasks_from_csv(self, file_path):
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header row

            for task_name, duration, priority in reader:
                self.add_task(task_name, int(duration), int(priority))
















# Create the list
tasks = LinkedList()

# Add tasks
tasks.add_task("Write report", 30, 2)
tasks.add_task("analyse data", 10, 3)
tasks.display_tasks()
print(tasks.find_task("analyse data"))
print(tasks.calculate_total_duration())

tasks.remove_task("Write report")
tasks.display_tasks()

# Print results










