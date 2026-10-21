history = []

current_page = input("Enter first page: ")
history.append(current_page)

operations = int(input("Enter number of operations: "))

for i in range(operations):
    operation = input("Enter operation (visit/back): ").lower()

    if operation == "visit":
        page = input("Enter page: ")
        history.append(page)
        current_page = page
        print("Current page:", current_page)

    elif operation == "back":
        if len(history) > 1:
            history.pop()
            current_page = history[-1]
            print("Current page:", current_page)
        else:
            print("Error: No previous page. Already at the first page.")

    else:
        print("Invalid operation")