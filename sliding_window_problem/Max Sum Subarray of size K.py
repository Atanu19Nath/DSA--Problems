class Solution:
    def maximumSumSubarray (self,arr,k):
        # code here 
        
        max_sum = float('-inf')
        
        i = 0
        j = 0
        sum = 0
        
        size = len(arr)
        
        while j < size:
            
            sum = sum + arr[j]
            
            if j-i+1 < k :
                j +=1
            
            elif j-i+1 == k :
                
                max_sum = max(max_sum, sum)
                sum = sum - arr[i]
                
                i +=1
                j +=1
        
        return max_sum