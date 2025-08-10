class Solution:
    def numberOfSubarrays(self, arr, target):
        # code here
        
        count = 0
        csum = 0
    
        prefix = {}
    
           
        for j in range(len(arr)):
    
    
            csum = csum + arr[j]
    
            if csum == target:
    
                count +=1
    
            if csum - target in prefix:
                
                count = count + prefix[csum-target]
    
            if csum in prefix:
    
                prefix[csum] +=1
            
            if csum not in prefix:
    
                prefix[csum] = 1
    
            
            
        return count 