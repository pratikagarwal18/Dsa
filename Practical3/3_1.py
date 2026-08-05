def bubble_sort(arr):
    a = arr[:]
    n = len(a)

    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a

def selection_sort(arr):
    a = arr[:]
    n = len(a)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]

    return a

def insertion_sort(arr):
    a = arr[:]
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a

n = int(input())
arr = list(map(int, input().split()))

print(bubble_sort(arr))
print(selection_sort(arr))
print(insertion_sort(arr))