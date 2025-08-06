class Solution:
    def maxFruits(self, arr, totalTime):
        # code here
        
        start = 0
        
        maxi = float('-inf')
        
        w_sum = 0
        
        for end in range(len(arr)):
            
            w_sum = w_sum + arr[end]
            
            if end - start + 1 == totalTime :
                
                maxi = max(w_sum, maxi)
                
                w_sum = w_sum - arr[start]
                
                start +=1
                
        
        if maxi == float('-inf'):
            
            a_sum = 0
            
            for i in arr:
                
                a_sum = a_sum + i
            
            return a_sum
            
        return maxi
