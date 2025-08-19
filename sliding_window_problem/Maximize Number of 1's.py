class Solution:
    def maxOnes(self, arr, k):
        # code here
        
        start = 0

        mp = {}
        
        countzero = 0
    
        maxlen = 0
    
        for end in range(len(arr)):
                
                if arr[end] in mp:
                     
                     mp[arr[end]] +=1
    
                if arr[end] not in mp:
                     
                     mp[arr[end]] = 1
        
                if arr[end] == 0:
                     
                     countzero +=1
    
                while countzero > k:
                     
                    mp[arr[start]] -=1
    
                    if mp[arr[start]] == 0:
                          
                        del mp[arr[start]]
    
                    if arr[start] == 0:
                          
                        countzero -=1
    
                    start +=1
                     
       
                if countzero <= k:
    
                    maxlen = max(maxlen,end - start + 1)
     
        return maxlen
            