class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.front
        self.front = new_node

        if self.rear is None:
            self.rear = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_front(data)
            return

        current = self.front

        for _ in range(position - 1):
            if current is None:
                break
            current = current.next

        if current is None:
            print("Position is greater than the current queue length.")
            return

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

        if new_node.next is None:
            self.rear = new_node

    def display(self):
        current = self.front

        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print()


queue = Queue()

n = int(input("Enter number of operations: "))

for _ in range(n):
    operation = input("Enter operation (front/end/position): ").lower()

    if operation == "front":
        value = int(input("Enter patient token: "))
        queue.insert_front(value)

    elif operation == "end":
        value = int(input("Enter patient token: "))
        queue.insert_end(value)

    elif operation == "position":
        value = int(input("Enter patient token: "))
        position = int(input("Enter position: "))
        queue.insert_at_position(value, position)

    else:
        print("Invalid operation.")
        continue

    queue.display()