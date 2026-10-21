n = int(input("Enter maximum capacity: "))

queue = [None] * n
front = -1
rear = -1

operations = int(input("Enter number of operations: "))

for i in range(operations):

    operation = input("Enter operation (join/serve): ").lower()

    # JOIN = Enqueue
    if operation == "join":
        token = input("Enter token: ")

        if rear == n - 1:
            print("Error: Queue is FULL. Cannot join.")
        else:
            if front == -1:
                front = 0

            rear += 1
            queue[rear] = token

            print("Front token:", queue[front])

    # SERVE = Dequeue
    elif operation == "serve":

        if front == -1 or front > rear:
            print("Error: Queue is EMPTY. Cannot serve.")
        else:
            queue[front] = None
            front += 1

            if front > rear:
                front = -1
                rear = -1
                print("Queue is EMPTY")
            else:
                print("Front token:", queue[front])

    else:
        print("Invalid operation")