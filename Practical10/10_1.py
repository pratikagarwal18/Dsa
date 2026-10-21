SLOTS = 10


def park(lot, reg):
    start = reg % SLOTS
    for step in range(SLOTS):
        spot = (start + step) % SLOTS
        if lot[spot] is None:
            lot[spot] = reg
            return spot
    return None


def main():
    n = int(input("Number of vehicles: "))
    regs = list(map(int, input("Enter registrations: ").split()))
    lot = [None] * SLOTS
    for reg in regs[:n]:
        spot = park(lot, reg)
        if spot is None:
            print("Lot full, no space for", reg)
        else:
            print(f"{reg} -> slot {spot}")
    print("Final parking lot:")
    for i, reg in enumerate(lot):
        print(f"Slot {i}: {reg if reg is not None else 'Empty'}")


main()