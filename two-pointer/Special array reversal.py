#User function Template for python3
import string

class Solution:
    def reverse(self, s):
        # code here

        special_char = string.punctuation

        k = 0

        list = []
        for i in s:
            list.append(i)
        
        j = len(list)-1

        while k < j :

            if list[k] not in special_char and list[j] not in special_char:

                list[k],list[j] = list[j],list[k]
                k +=1
                j -=1
            elif list[k] in special_char:

                k +=1
            elif list[j] in special_char:

                j -=1

        ans = ""

        for i in list:
            ans = ans + i
            
        return ans

s = Solution()

print(s.reverse("A&X#"))