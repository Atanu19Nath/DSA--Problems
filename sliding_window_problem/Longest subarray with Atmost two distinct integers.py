class Solution:
    def totalElements(self, arr):
        # Code here
        
        start = 0
        
        mp = {}
        
        maxlen = float('-inf')
        
        
        for end in range (len(arr)):
            
            if arr[end] in mp:
                
                mp[arr[end]] +=1
                
            if arr[end] not in mp:
                
                mp[arr[end]] = 1
                
            
            while len(mp) > 2:
                
                mp[arr[start]] -=1
                
                if mp[arr[start]] == 0:
                    
                    del mp[arr[start]]
                    
                start +=1
                
                
            
                
                
            maxlen = max(maxlen,end-start+1)
            
        return maxlen
            
            