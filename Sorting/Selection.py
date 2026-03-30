def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        # find minimum element
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # swap only if needed 
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


# Input
arr = list(map(int, input("Enter numbers: ").split()))

# Output
print("Sorted array:", selection_sort(arr))