from collections import deque


def build_map(n, roads):
    city = {i: [] for i in range(n)}
    for a, b in roads:
        city[a].append(b)
        city[b].append(a)
    for i in city:
        city[i].sort()
    return city


def deep_team(city, start):
    seen = set()
    order = []
    stack = [start]
    while stack:
        building = stack.pop()
        if building in seen:
            continue
        seen.add(building)
        order.append(building)
        for nxt in reversed(city[building]):
            if nxt not in seen:
                stack.append(nxt)
    return order


def wide_team(city, start):
    seen = {start}
    order = []
    queue = deque([start])
    while queue:
        building = queue.popleft()
        order.append(building)
        for nxt in city[building]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return order


def main():
    n = int(input("Number of buildings: "))
    m = int(input("Number of roads: "))
    roads = []
    print("Enter roads (u v):")
    for _ in range(m):
        a, b = map(int, input().split())
        roads.append((a, b))
    start = int(input("Starting building: "))
    city = build_map(n, roads)
    print("DFS order:", *deep_team(city, start))
    print("BFS order:", *wide_team(city, start))


main()