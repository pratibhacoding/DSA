def counting_sort(arr):
    if len(arr) == 0:
        return arr

    min_val = min(arr)
    max_val = max(arr)

    k = max_val - min_val + 1  # k is the range of input values
    count = [0] * k
    output = [0] * len(arr)

    #  Count frequency
    for num in arr:
        count[num - min_val] += 1

    #  Prefix sum (cumulative count)
    for i in range(1, k):
        count[i] += count[i - 1]

    # Build output (stable)
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output


# Input
arr = list(map(int, input("Enter numbers: ").split()))

#s Output
print("Sorted array:", counting_sort(arr))