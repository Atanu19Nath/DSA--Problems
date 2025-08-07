#User function Template for python3

class Solution:
    def modify(self, s):
        # code here
        
        list1 = []
        
        for i in s:
        
            if i != ' ':
                list1.append(i)
        
        
        
        return ''.join(list1)