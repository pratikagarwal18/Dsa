class Student:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None


class SinglyCircle:
    def __init__(self):
        self.head = None
        self.size = 0

    def join(self, name, position):
        if position < 1 or position > self.size + 1:
            return False

        student = Student(name)

        if self.head is None:
            student.next = student
            self.head = student
        elif position == 1:
            last = self.head
            while last.next is not self.head:
                last = last.next
            student.next = self.head
            last.next = student
            self.head = student
        else:
            before = self.head
            for _ in range(position - 2):
                before = before.next
            student.next = before.next
            before.next = student

        self.size += 1
        return True

    def leave(self, name):
        if self.head is None:
            return False

        before = self.head
        while before.next is not self.head:
            before = before.next

        current = self.head
        found = False
        for _ in range(self.size):
            if current.name == name:
                found = True
                break
            before = current
            current = current.next

        if not found:
            return False

        if self.size == 1:
            self.head = None
        else:
            before.next = current.next
            if current is self.head:
                self.head = current.next

        self.size -= 1
        return True

    def show(self):
        if self.head is None:
            return "Circle is empty"

        names = []
        current = self.head
        for _ in range(self.size):
            names.append(current.name)
            current = current.next
        return " -> ".join(names) + f" -> (back to {self.head.name})"


class DoublyCircle:
    def __init__(self):
        self.head = None
        self.size = 0

    def join(self, name, position):
        if position < 1 or position > self.size + 1:
            return False

        student = Student(name)

        if self.head is None:
            student.next = student
            student.prev = student
            self.head = student
        else:
            target = self.head
            for _ in range(position - 1):
                target = target.next
            before = target.prev

            student.prev = before
            student.next = target
            before.next = student
            target.prev = student

            if position == 1:
                self.head = student

        self.size += 1
        return True

    def leave(self, name):
        if self.head is None:
            return False

        current = self.head
        found = False
        for _ in range(self.size):
            if current.name == name:
                found = True
                break
            current = current.next

        if not found:
            return False

        if self.size == 1:
            self.head = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            if current is self.head:
                self.head = current.next

        self.size -= 1
        return True

    def show(self):
        if self.head is None:
            return "Circle is empty"

        names = []
        current = self.head
        for _ in range(self.size):
            names.append(current.name)
            current = current.next
        return " <-> ".join(names) + f" <-> (back to {self.head.name})"

    def show_reverse(self):
        if self.head is None:
            return "Circle is empty"

        names = []
        current = self.head.prev
        for _ in range(self.size):
            names.append(current.name)
            current = current.prev
        return " <-> ".join(names)


def main():
    singly = SinglyCircle()
    doubly = DoublyCircle()

    operations = [
        ("join", "Asha", 1),
        ("join", "Ravi", 2),
        ("join", "Meera", 3),
        ("join", "Kabir", 2),
        ("join", "Nina", 1),
        ("join", "Zoya", 9),
        ("display",),
        ("leave", "Kabir"),
        ("leave", "Nina"),
        ("leave", "Meera"),
        ("leave", "Ghost"),
        ("leave", "Ravi"),
        ("leave", "Asha"),
        ("leave", "Asha"),
        ("join", "Dev", 1),
        ("display",),
    ]

    for step, op in enumerate(operations, start=1):
        action = op[0]

        if action == "join":
            name, position = op[1], op[2]
            done_singly = singly.join(name, position)
            done_doubly = doubly.join(name, position)
            if done_singly and done_doubly:
                message = f"{name} joins at position {position}"
            else:
                message = f"{name} could not join, position {position} is not valid"
        elif action == "leave":
            name = op[1]
            done_singly = singly.leave(name)
            done_doubly = doubly.leave(name)
            if done_singly and done_doubly:
                message = f"{name} leaves the circle"
            else:
                message = f"{name} is not in the circle"
        else:
            message = "Showing the circle"

        print(f"{step}. {message}")
        print(f"   Singly : {singly.show()}")
        print(f"   Doubly : {doubly.show()}")
        print(f"   Reverse: {doubly.show_reverse()}\n")


if __name__ == "__main__":
    main()