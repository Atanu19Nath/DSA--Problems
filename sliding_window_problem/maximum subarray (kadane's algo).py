class Solution:
    def maxSubarraySum(self, nums):
        
    

        maxsum = float('-inf')

        csum = 0

        for i in range(len(nums)):

            csum = csum + nums[i]

            maxsum = max(maxsum,csum)

            if csum < 0 :

                csum = 0

        return maxsum


        