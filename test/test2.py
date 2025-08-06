from collections import Counter

class Solution:
    def countSubstr (self, str, k):
        # Code here
        
        mp = {}
        
        count  = 0
        
        arr = []
        
        for i in str:
            
            arr.append(i)
        
        # print(arr)
        start  = 0
        
        for end in range(len(arr)):
            
            if arr[end] in mp:
                
                mp[arr[end]] +=1
                
            if arr[end] not in mp:
                
                mp[arr[end]] = 1
        
            if len(mp)  == k:
                
                count +=1
                
            while len(mp) > k:
                
                mp[arr[start]] -=1
                
                if mp[arr[start]] == 0:
                    
                    del mp[arr[start]]

                    count +=1
                    
                start += 1

            
            
        # mp2 = Counter(arr)

        # if len(mp2) == k :

        #     count +=1

        return count
    


s = Solution()


str = "aabcbebebe"
print(s.countSubstr(str,1))