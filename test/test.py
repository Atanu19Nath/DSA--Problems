class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:



        set1 = set()

        start = 0

        max_count = 0

        for end in range(len(str)) :
        
        
            if str[end] in set1:

                while str[end] in set1:

                    set1.remove(str[start])

                    start +=1

                set1.add(str[end])

            if str[end] not in set1:

                set1.add(str[end])

            
            
            max_count = max(max_count,end-start+1)



        return max_count
        





# str = "abcabcbb"

# str = "bbbbb"

str = "pwwkew"

s = Solution()

print(s.lengthOfLongestSubstring(str))





