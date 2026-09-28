class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.front
        self.front = new_node

        if self.rear is None:
            self.rear = new_node

    def delete_by_value(self, value):
        if self.front is None:
            print("Queue is empty.")
            return

        if self.front.data == value:
            self.front = self.front.next

            if self.front is None:
                self.rear = None

            return

        current = self.front

        while current.next is not None:
            if current.next.data == value:
                if current.next == self.rear:
                    self.rear = current

                current.next = current.next.next
                return

            current = current.next

        print("Value not found.")

    def display_forward(self):
        current = self.front

        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print()

    def display_reverse(self):
        self._reverse_print(self.front)
        print()

    def _reverse_print(self, node):
        if node is None:
            return

        self._reverse_print(node.next)
        print(node.data, end=" ")


queue = Queue()

n = int(input("Enter number of patients: "))

for _ in range(n):
    value = int(input("Enter patient token: "))
    queue.insert_end(value)

while True:
    print("\n1. Delete by value")
    print("2. Reverse printing")
    print("3. Forward traversal")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter patient token to delete: "))
        queue.delete_by_value(value)

    elif choice == 2:
        queue.display_reverse()

    elif choice == 3:
        queue.display_forward()

    elif choice == 4:
        break

    else:
        print("Invalid choice.")