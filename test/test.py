class Solution:
    def countSubarrays(self, arr, k):
        # Code here
        
        
        set1 = []
        
        count_sa = 0
        for start in range(len(arr)):

            mp = {}
            count = 0
            
            for end in range(start,len(arr)):
                
                if arr[end] not in mp:
                    
                    mp[arr[end]] = 1
                else:
                    
                    mp[arr[end]] +=1
                
                if arr[end] % 2 != 0:
                    
                    count +=1
                    
                while count == k:
                    
                    if [start,end] not in set1:
                        
                        set1.append([start,end])

                        count_sa +=1  

                    
                    mp[arr[start]] -= 1  #
                            
                    if mp[arr[start]] == 0: #
                            
                        if arr[start] % 2!=0: #
                                
                            count -=1      #
                            
                        del mp[arr[start]]  #
                        
                    
                    start +=1    
                
        return count_sa
    
s = Solution()

arr = [2, 2, 5, 6, 9, 2, 11]
k = 2

print(s.countSubarrays(arr,k))