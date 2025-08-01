from collections import Counter

class Solution:
    def intersect(self, a, b):
        # code here
        
        if len(a) == 0 or len(b) == 0:
            
            return []

        a.sort()
        b.sort()
    

        i = 0
        j = 0

        ans_list = {}

        while i < len(a) and j < len(b):

            if a[i] == b[j]:

                if a[i] not in ans_list:
                    ans_list[a[i]] = 1
                
                i += 1
                j += 1

            elif a[i] < b[j]:
                i +=1
            elif b[j] < a[i]:
                j +=1

        return ans_list




s = Solution()

a = [1, 2, 1, 3, 1]
b = [3, 1, 3, 4, 1]

print(s.intersect(a,b))