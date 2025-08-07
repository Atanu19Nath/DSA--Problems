#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        
        s1 = list(s)
        
        i = 0
        j = len(s1)-1
        
        while i < j:
            
            s1[i],s1[j] = s1[j],s1[i]
            
            i +=1
            j -=1
        
        s2 = ''.join(s1)  
        
        return s2