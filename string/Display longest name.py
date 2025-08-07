
class Solution:
    def longest(self, arr):
        # code here
        
        count = len(arr[0])
        ans = arr[0]
        
        for i in range(1, len(arr)):
                
            if len(arr[i]) > count:
                
                count = len(arr[i])
                ans = arr[i]
                
        return ans