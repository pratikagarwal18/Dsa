SIZE = 10


def first_slot(student):
    return student % SIZE


def jump_size(student):
    return 7 - (student % 7)


def assign(table, student):
    start = first_slot(student)
    jump = jump_size(student)
    for attempt in range(SIZE):
        slot = (start + attempt * jump) % SIZE
        if table[slot] is None:
            table[slot] = student
            return slot, jump, attempt
    return None, jump, SIZE


def main():
    n = int(input("Number of students: "))
    ids = list(map(int, input("Enter student IDs: ").split()))
    table = [None] * SIZE
    for student in ids[:n]:
        slot, jump, tries = assign(table, student)
        if slot is None:
            print(f"{student} -> no free slot found (jump {jump})")
        else:
            print(f"{student} -> slot {slot} (jump {jump}, collisions {tries})")
    print("Final table:")
    
    for i, student in enumerate(table):
        print(f"Slot {i}: {student if student is not None else 'Empty'}")


main()