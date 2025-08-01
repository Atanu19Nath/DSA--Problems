
class Solution:
    def isBalanced(self, s):
        # code here
        if len(s) == 0:
            return False
            
        list = []
        
        list.append(s[0])
        
        for i in range(1,len(s)):
            
            ans = s[i]
            size = len(list)
            if size > 0:
                if (s[i] == ')' and list[size-1] == '(') or (s[i] == '}' and list[size-1] == '{') or (s[i] == ']' and list[size-1] == '['):
                    
                    a = list.pop()
                    
                else:
                    list.append(s[i])
            else:
                list.append(s[i])
        if len(list) == 0:
            return True
        else: 
            return False
        

s = Solution()

print(s.isBalanced("[]}}]]])){}{}}[}}]}["))