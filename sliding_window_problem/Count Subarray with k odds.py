class Solution:
    
    
    def atmostk(self,arr,k):
        
        start = 0
        countodd = 0
        
        count = 0
        
        
        for end in range(len(arr)):
            
            if arr[end] % 2 != 0:
                countodd +=1
            
            
            while countodd > k:
                    
                if arr[start] % 2 !=0:
                        
                    countodd -=1
                start +=1
            
            count = count + end -start +1
            
        return count
            
            
    
    def countSubarrays(self, arr, k):
        # Code here
        
        r1 = self.atmostk(arr,k) 
        
        r2 = self.atmostk(arr,k-1)
        
        
        # print(r1,r2)
        
        return r1-r2
        