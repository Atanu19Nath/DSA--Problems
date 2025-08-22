class Solution:
    def maxSubArray(self,arr):

        maxsum = float('-inf')
        for i in range(len(arr)):

            sum = 0

            for j in range(i,len(arr)):

                sum = sum + arr[j]

                maxsum = max(maxsum,sum)

        return maxsum



s = Solution()
arr = [-2,1,-3,4,-1,2,1,-5,4]

print(s.maxSubArray(arr))