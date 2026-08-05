arr = list(map(int,input().split()))
count0 = count1 = count2 = 0

for x in arr:
    if x == 0:
        count0 += 1
    elif x == 1:
        count1 += 1
    else:
        count2 += 1

i = 0

while count0 > 0:
    arr[i] = 0
    i += 1
    count0 -= 1

while count1 > 0:
    arr[i] = 1
    i += 1
    count1 -= 1

while count2 > 0:
    arr[i] = 2
    i += 1
    count2 -= 1

print(arr)