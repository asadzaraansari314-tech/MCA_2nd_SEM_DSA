# Binary Search using Divide and Conquer

def binary_search(arr, low, high, key):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        elif key < arr[mid]:
            return binary_search(arr, low, mid - 1, key)

        else:
            return binary_search(arr, mid + 1, high, key)

    return -1

# Sorted list
arr = [10, 20, 30, 40, 50, 60, 70]

key = 40

result = binary_search(arr, 0, len(arr) - 1, key)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
