SHELVES = 10


def place(shelves, code):
    shelves[code % SHELVES].append(code)


def main():
    n = int(input("Number of books: "))
    codes = list(map(int, input("Enter book codes: ").split()))
    shelves = [[] for _ in range(SHELVES)]
    for code in codes[:n]:
        place(shelves, code)
    print("Final shelf contents:")
    for i, stack in enumerate(shelves):
        print(f"Shelf {i}:", " -> ".join(map(str, stack)) if stack else "Empty")


main()