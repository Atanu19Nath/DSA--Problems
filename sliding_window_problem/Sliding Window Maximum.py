from collections import deque


class Solution:
    def maxSlidingWindow(self, arr, k) :
        

        start = 0

        maximum = float("-inf")

        result = []

        ans = deque()

        for end in range(len(arr)):

            if len(ans) == 0:

                ans.append(end)

            else:
            
                while ans and arr[end] > arr[ans[-1]]:


                    ans.pop()

                ans.append(end)
                                

            if end - start + 1 == k:

                result.append(arr[ans[0]])

                if start == ans[0]:

                    ans.remove(start)
                start +=1
    
        return result
    
s = Solution()

nums = [1,3,-1,-3,5,3,6,7]
# nums = [1,3,1,2,0,5]
k = 3

print(s.maxSlidingWindow(nums,k))
            