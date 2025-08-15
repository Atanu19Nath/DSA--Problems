#User function Template for python3

class Solution:
    
    
    def atmostk(self,arr,k):
        
        start = 0
        
        mp = {}
        
        count = 0
        
        for end in range(len(arr)):
            
            if arr[end] in mp:
                
                mp[arr[end]] +=1
                
            if arr[end] not in mp:
                
                mp[arr[end]] = 1
                
            while len(mp) > k:
                
                mp[arr[start]] -=1
                
                if mp[arr[start]] == 0:
                    
                    del mp[arr[start]]
                    
                start +=1
                
            
            count = count + end - start +1
        
        return count
            
    
    
    def countDistinctSubarray(self,arr, n): 
        #code here.
        
        set1 = set()
        
        for i in range (n):
            
            set1.add(arr[i])
            
    
        k = len(set1)
       
        return self.atmostk(arr,k) - self.atmostk(arr,k-1)
        
        
        
        
        
        
        