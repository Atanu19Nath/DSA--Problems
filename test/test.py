def searchInsert(nums, target) -> int:

    start = 0

    end = len(nums) - 1

    while start <= end:

        mid = start + ( end - start)//2
        
        print(start , mid, end )

        if nums[mid] == target:

            return mid

        elif target > nums[mid-1] and target < nums[mid]:

            return mid

        elif target > nums[mid]:

            start = mid + 1
        
        else:

            end = mid - 1
            
    if target > nums[len(nums) -1]:
        
        print("this one")
    elif target < nums[0]:
        
        return 0
    
    else:
        return -1

nums = [1,3,5,6]

print(nums)
target = 0

print(searchInsert(nums,target))