class Solution:
    def zeroFilledSubarray(self,nums):

        count = 0

        list1 = {}

        start = 0


        for end in range(len(nums)):


            if nums[end] == 0:

                count = count + end - start + 1

            elif nums[end] != 0:

                while nums[end] != 0:

                    end +=1

                    if end !


        return count


    

s = Solution()

# nums = [0,0,0,2,0,0]

# nums = [1,3,0,0,2,0,0,4]

nums = [2,10,2019]


print(s.zeroFilledSubarray(nums))