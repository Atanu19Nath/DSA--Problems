class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        
        
        lenght = float('-inf')
        
        
        c_sum =0
        
        mp = {}
        
        for end in range (len(arr)):
            
            c_sum = c_sum + arr[end]
            
            if c_sum == k:
                
                lenght = max(lenght, end + 1)
            
            if c_sum - k in mp:
            
                s = mp[c_sum - k] + 1
                lenght = max(lenght, end - s +1 )
            
            if c_sum not in mp:
                
                mp[c_sum] = end
        
        
        if lenght == float('-inf'):
            
            return 0
            
        else:
            return lenght
            
            
    
