class Solution:
    def longestUniqueSubstr(self, s):


        set1 = set()

        start = 0

        length = float('-inf')

        for end in range( len(s)):

            while s[end] in set1:

                set1.remove(s[start])

                start +=1

            set1.add(s[end])   

            length = max(length,end-start+1)

        return length


            


        
s = Solution()

str = "cadbzazbcd"

print(s.longestUniqueSubstr(str))








# BRUTE FORCE METHOD  O(N2)

# class Solution:
#     def longestUniqueSubstr(self, s):
        
#         count = 0

#         maxlen = float('-inf')

#         for i in range(len(s)):

#             s1 = s[i] 
#             for j in range(i+1, len(s)):


#                 if s[j] in s1:
#                     break

#                 s1 = s1 + s[j]
                
#                 maxlen = max(maxlen,j - i + 1)
            
#         print(maxlen)


            


        
# s = Solution()

# str = "cadbzazbcd"

# s.longestUniqueSubstr(str)