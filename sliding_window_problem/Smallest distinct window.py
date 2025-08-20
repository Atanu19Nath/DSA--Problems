#User function Template for python3

class Solution:
    def findSubString(self, s):
        # code here
        
        start = 0

        mp = {}
        
        set1 = set()
    
        minlen = float('inf')
    
        for i in s:
    
            set1.add(i)
    
        for end in range(len(s)):
    
            if s[end] in mp:
    
                mp[s[end]] +=1
    
            if s[end] not in mp:
    
                mp[s[end]] = 1
    
            while len(mp) == len(set1):    
                    
                    minlen = min(minlen, end - start +1)
    
                    mp[s[start]] -=1
    
                    if mp[s[start]] == 0:
                         
                         del mp[s[start]]
    
                    start +=1
    
    
        return minlen 
        
        
        