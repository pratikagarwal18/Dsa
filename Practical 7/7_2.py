from collections import deque

q = deque()

n = int(input("Enter number of operations: "))

for i in range(n):
    operation = input("Enter operation (arrive/attend): ")

    if operation == "arrive":
        patient = input("Enter patient name: ")
        q.append(patient)

    elif operation == "attend":
        if q:
            q.popleft()
        else:
            print("Ward is empty")

    if q:
        print("Front patient:", q[0])
    else:
        print("Front patient: None")