def longestKSubstr(s):
    
    count = 0
    
    start = 0
    m = 1
    mp = {}

    for end in range(len(s)):

        if s[end] in mp:

            mp[s[end]] +=1

        if s[end] not in mp:

            mp[s[end]] = 1

        while len(mp) == 3:

            count += len(s) - end

            mp[s[start]] -= 1

            if mp[s[start]] == 0:
                del mp[s[start]]
            start += 1

    
    print(count)

        
s = "abcabc"
longestKSubstr(s)


# BRUTE FORCE


# def longestKSubstr(s):
    
#     count = 0
#     for i in range(len(s)):

#         set1 = set()

#         for j in range(i, len(s)):

#             set1.add(s[j])

#             if len(set1) == 3:

#                 count = count + len(s) - j
#                 break
    
#     print(count)

        
# s = "aabcabc"
# longestKSubstr(s)