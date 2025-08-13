class Solution:
    def substrCount(self, s, k):
        # code here
        
        count = 0

        start = 0
    
        mp = {}
    
    
        for end in range(len(s)):
                
                if s[end] in mp:
                     
                     mp[s[end]] +=1
    
                if s[end] not in mp:
                     
                     mp[s[end]] = 1
       
                if end - start + 1 == k:
    
                    if len(mp) == k-1:
    
                        count +=1
                    
                    mp[s[start]] -=1
    
                    if mp[s[start]] == 0:
                         del mp[s[start]]
                    
                    start +=1
                    
        return count
            