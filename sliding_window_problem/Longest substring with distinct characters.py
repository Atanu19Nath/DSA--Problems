class Solution:
    def longestUniqueSubstr(self, s):


        set1 = set()

        start = 0

        length = 0

        for end in range( len(s)):

            while s[end] in set1:

                set1.remove(s[start])

                start +=1

            set1.add(s[end])   

            length = max(length,end-start+1)

        return length