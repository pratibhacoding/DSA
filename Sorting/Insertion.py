def insertion_sort(arr):
    n = len(arr)

    for i in range(1,n):
        key = arr[i]
        j = i - 1
        
        #  shift elements instead of multiple swaps
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key   # place key at correct position
    
    return arr


#  Input
arr = list(map(int, input("Enter numbers: ").split()))

#  Output
print("Sorted array:", insertion_sort(arr))