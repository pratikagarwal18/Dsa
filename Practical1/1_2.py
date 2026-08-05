n = int(input())
arr = list(map(int, input().split()))

freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1

for key in freq:
    if freq[key] > 1:
        print(key, end=" ")