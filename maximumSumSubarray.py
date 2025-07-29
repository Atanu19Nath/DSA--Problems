class Solution:
    def maximumSumSubarray (self,arr,k):
        # code here 
        
        i = 0
        j = 0
        size = len(arr)
        sum = 0
        
        ans = float('-inf')
        
        while j < size :
            
            sum  = sum + arr[j]
            
            
            if j - i + 1 < k :
                
                j += 1
            
            elif j - i + 1 == k :
                
                ans = max(ans, sum)
                sum = sum - arr[i]
                
                i += 1
                j += 1
                
        return ans
    
arr = [100,200,300,400]

k = 2

obj = Solution()

print(obj.maximumSumSubarray(arr,k))