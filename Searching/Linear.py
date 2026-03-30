def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# User input for list
arr = list(map(int, input("Enter elements: ").split()))

# User input for target
target = int(input("Enter element to search: "))

# Function call
result = linear_search(arr, target)

# Output
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")