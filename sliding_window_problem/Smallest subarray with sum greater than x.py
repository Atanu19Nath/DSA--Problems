class Solution:
    def smallestSubWithSum(self, x, arr):
        # Your code goes here 
        
        count = 0
        start = 0
        smallest = float('inf')
        window_sum = 0
        size = len(arr)
        
        for end in range(size):
            
            window_sum = window_sum + arr[end]
            
            while window_sum > x :
                
               
                smallest = min(smallest, end-start+1)
                window_sum = window_sum - arr[start]
                
                start +=1
            
            
        
        if smallest == float('inf'):
            return 0
        else:
            return smallest
            
            
        
        
        
