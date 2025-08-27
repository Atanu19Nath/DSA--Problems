def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1
        if nums[i] != nums[correct_index]:
            # Swap to correct place
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    return nums


arr = [3, 1, 5, 4,2]

print(cyclic_sort(arr))