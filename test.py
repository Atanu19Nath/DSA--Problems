
class Solution:
    def findMaxSubarraySum(self, arr, x):
        # Your code goes here
        
        c_sum = 0
        
        start = 0
        
        maxi = float('-inf')
        
        for end in range(len(arr)):
            
            c_sum = c_sum + arr[end]
            
            if c_sum <= x :
                
                maxi = max(maxi,c_sum)
                print("maximum =",maxi)

            while c_sum > x:

                c_sum = c_sum - arr[start]

                start +=1

            
                
        return maxi
    
s = Solution()

arr = [1, 2, 3, 4, 5]
x = 11 

print(s.findMaxSubarraySum(arr,x))
                
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # i = 0
        # j = 0
        
        # sum = 0
        # maxi = float('-inf')
        
        # while (j < len(arr)):
            
        #     if sum + arr[j] <= x:
                
        #         sum = sum + arr[j]
        #         maxi = max(maxi, sum) 
        #         j +=1
            
        #     elif sum + arr[j] > x:

                
        #         sum = sum - arr[i]
                
        #         i +=1
        
            
        
        # return maxi
            