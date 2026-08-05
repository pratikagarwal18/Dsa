def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def recursive_search(arr, target, index=0):
    if index == len(arr):
        return -1
    if arr[index] == target:
        return index
    return recursive_search(arr, target, index + 1)

n = int(input())
arr = input().split()
target = input()

print(linear_search(arr, target))
print(recursive_search(arr,target))
