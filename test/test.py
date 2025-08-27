def all_missing_numbers(arr):
    i = 0
    n = len(arr)

    while i < n:
        correct_index = arr[i]
        if arr[i] < n and arr[i] != arr[correct_index]:
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
        else:
            i += 1

    missing = []
    for i in range(n):
        if arr[i] != i:
            missing.append(i)

    return missing

# Example
arr = [4,0,3,1,2,6,7,8,9,10,12,13,15]
print(all_missing_numbers(arr))   # [5, 11, 14]
