def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[low]   # 🔹 first element as pivot
    i = low + 1

    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # place pivot at correct position
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1


# 🔹 Input
arr = list(map(int, input("Enter numbers: ").split()))

# 🔹 Call quick sort
quick_sort(arr, 0, len(arr) - 1)

# 🔹 Output
print("Sorted array:", arr)