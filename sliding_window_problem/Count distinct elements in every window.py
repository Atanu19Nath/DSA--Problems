class Solution:
    def countDistinct(self, arr, k):
        # Code here
        
        start = 0

        mp = {}
        list2 = []
        for end in range(len(arr)):
    
            if arr[end] in mp:
    
                mp[arr[end]] +=1
    
            if arr[end] not in mp:
    
                mp[arr[end]] = 1
    
            if end - start + 1 == k:
    
                list2.append(len(mp))
    
                mp[arr[start]] -=1
    
                if mp[arr[start]] == 0:
    
                    del mp[arr[start]]
    
                start +=1
            
        return list2
            
        
            
            