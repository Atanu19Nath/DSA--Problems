from collections import Counter

class Solution:
    def substrWithVowels(self, s1, s2):
        # code here
        
        
        start = 0
        count = 0
        mp1 = Counter(s1)
        mp2 = {}
        set1 = set()
        mini = float('inf')
        
        for end in range(len(s2)):
            
            if s2[end] in mp2:
                
                mp2[s2[end]] +=1
            else:
                
                mp2[s2[end]] = 1
                
            
            if s2[end] in mp1:
                
                set1.add(s2[end])
                
            while len(set1) == len(mp1):
                
                mini = min(mini, end- start +1)
                
                mp2[s2[start]] -= 1
                
                if mp2[s2[start]] == 0:
                
                    if s2[start] in mp1:
                        
                        set1.remove(s2[start])
                    
                    del mp2[s2[start]]
                start +=1
                    
        if mini == float('inf'):
            return -1
        else:
            return mini

s = Solution()
s1 = "ae"
s2 = "acbaudeq"
print(s.substrWithVowels(s1,s2))       
                