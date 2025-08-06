#User function Template for python3

class Solution:
    def smallestSubstring(self, s):
        # Code here
        
        list1 = []
        
    
        for i in s:
            list1.append(int(i))
    
    
        k = 3
        mp1 = {1:1,0:1,2:1}
        mp2 = {}
        small = float('inf')
        start = 0
    
        for end in range(len(list1)):
    
            if list1[end] not in mp2:
                    
                mp2[list1[end]] = 1
                    
            elif list1[end] in mp2: 
    
                mp2[list1[end]] += 1   
    
    
            while len(mp1) == len(mp2):
                
                small = min(small, end - start+1)
        
                mp2[list1[start]] -= 1 
                
                if mp2[list1[start]] == 0:
        
                    del mp2[list1[start]]
                    
                start +=1
                
        if small == float('inf'):
            return -1
        else:
            return small

s = Solution()

str = "10212"

print(s.smallestSubstring(str))


