def next_greater_elements(nums):
    n = len(nums)
    
    stack = [nums[-1]]

    nums[-1] = -1

    for i in range(n-2,-1,-1):

        val = nums[i]         

        while stack and val >= stack[-1] :

            stack.pop()

        if len(stack) == 0:

            nums[i] = -1
        else:

            nums[i] = stack[-1]

        stack.append(val)      

    return nums



# Example
print(next_greater_elements([2,1,2,4,3]))  # [4,2,4,-1,-1]
