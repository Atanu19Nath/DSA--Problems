def missing_number(nums):
    i = 0
    n = len(nums)
    while i < n:
        correct_index = nums[i]
        if nums[i] < n and nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    print(nums)
    for i in range(n):
        if nums[i] != i:
            return i
    

    return n


arr = [4,0,3,1]

print(missing_number(arr))

