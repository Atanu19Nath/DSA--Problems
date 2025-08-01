
class Solution:
    def findMaxSubarraySum(self, arr, x):
        # Your code goes here
        
        i = 0
        j = 0
        
        sum = 0
        maxi = float('-inf')
        
        while (j < len(arr)):
            
            if sum + arr[j] <= x:
                
                sum = sum + arr[j]
                maxi = max(maxi, sum) 
                j +=1
            
            elif sum + arr[j] > x:

                
                sum = sum - arr[i]
                
                i +=1
        
            
        
        return maxi
    

s = Solution()

print(s.findMaxSubarraySum([1, 2, 3, 4, 5],11))
