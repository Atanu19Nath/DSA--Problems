class Solution:
    def removeConsecutiveCharacter(self, s):
        # code here
        if not s:
            return s
            
        result = [s[0]]
          
        j = 1
        
        while j < len(s):
        
            if s[j] != s[j-1]:
                result.append(s[j])
            
            j +=1
                
                
        s2 = ""
        for i in result:
        
            s2 = s2 + i
        
        return s2
    

s = Solution()

print(s.removeConsecutiveCharacter("aaaaaaabbbbbb"))