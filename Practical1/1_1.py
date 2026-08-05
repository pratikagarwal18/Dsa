n = int(input())
arr = list(map(int, input().split()))
h = int(input())

h %= n

result = arr[h:] + arr[:h]

print(*result)