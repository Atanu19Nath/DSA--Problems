#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr):
        ##Your code here
        #Return true or false
        
        c_sum = 0
        
        sum = 0
        
        mp = {}
        
        for i in range(len(arr)):
            
            c_sum = c_sum + arr[i]
            
            if c_sum == sum:
                
                return True
            
            if c_sum - sum in mp:
                
                return True
                
            if c_sum - sum not in mp:
                
                mp[c_sum] = 1
                
        
        return False
            
            