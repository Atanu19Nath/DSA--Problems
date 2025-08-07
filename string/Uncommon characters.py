#User function Template for python3

class Solution:
    # Function to find uncommon characters between two strings.
    def uncommonChars(self, s1, s2):
        #code here
        set1 = set(s1)
        set2 = set(s2)
        s = ""
        for i in set1:
                    
            if i not in s2:
                        
                s = s + i
                        
        for i in set2:
                    
            if i not in s1:
                        
                s = s + i
        
        if s == "":
            return s
        else: 
            return ''.join(sorted(s))
        