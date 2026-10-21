class Book:
    def __init__(self, code):
        self.code = code
        self.left = None
        self.right = None


class Shelf:
    def __init__(self):
        self.root = None

    def add(self, code):
        new_book = Book(code)
        if self.root is None:
            self.root = new_book
            return
        current = self.root
        while True:
            if code < current.code:
                if current.left is None:
                    current.left = new_book
                    return
                current = current.left
            elif code > current.code:
                if current.right is None:
                    current.right = new_book
                    return
                current = current.right
            else:
                return

    def inorder(self):
        result = []
        stack = []
        current = self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.code)
            current = current.right
        return result


def main():
    n = int(input("Number of books: "))
    codes = list(map(int, input("Enter book codes: ").split()))
    shelf = Shelf()
    for code in codes[:n]:
        shelf.add(code)
    order = shelf.inorder()
    print("Inorder sequence:", *order)
    ok = all(order[i] < order[i + 1] for i in range(len(order) - 1))
    print("Strictly increasing:", ok)


main()