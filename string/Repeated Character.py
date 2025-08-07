#User function Template for python3
from collections import Counter

class Solution:
    def firstRep(self, s):
        # code here
        
        mp = Counter(s)
        
        
        
        for i in s:
            
            if mp[i] > 1:
                
                return i
        
        
        return -1
                
                
        
        
        
                
                
                