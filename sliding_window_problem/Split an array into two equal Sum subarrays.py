class Solution:
    def canSplit(self, arr):
        #code here
        
        
        mp = []
        c_sum = 0
        
        for i in range(len(arr)):
            
            c_sum = c_sum + arr[i]
            
            mp.append(c_sum)
            
        
        if mp[len(arr)-1] / 2 in mp:
            
            return True
            
        return False