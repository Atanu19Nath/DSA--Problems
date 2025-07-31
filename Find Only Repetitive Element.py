#User function Template for python3
from collections import Counter
class Solution:
    def findDuplicate(self, arr):
        #code here
        
        ans = Counter(arr)
        
        for i in range(len(ans)):

            if ans[arr[i]] > 1:

                return arr[i]

            
        
s = Solution()

print(s.findDuplicate([1,3,2,3,4]))