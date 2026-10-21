n = int(input("Enter maximum capacity : "))

stack =[]
top = -1
operations = int(input("enter no of operations: "))

for i in range(operations):
    operation = input("enter the operation(place/take): ").lower()

    if operation == "place":
        tray = input("enter tray name: ")

        if top == n-1:
            print("error! the stack is empty!")

        else:
            stack.append(tray)
            top += 1
            print("Top tray:" ,stack[top])

    elif operation == "take":
        if top == -1:
            print("stack is empty!")
        else:
            stack.pop()
            top += -1
            print("top is popped!")

            if top == -1:
                print("stack is now empty")
            else:
                print("stack top tray:" , stack(top))
    else:
        print("invalid operation")
