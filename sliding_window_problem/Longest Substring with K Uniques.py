def longestKSubstr(s,k):
    
    maxlength = -1

    mp = {}

    start = 0

    for end in range(len(s)):

        if s[end] in mp:

            mp[s[end]] +=1

        if s[end] not in  mp:

            mp[s[end]] = 1   

        while len(mp) > k:

            mp[s[start]] -= 1

            if mp[s[start]] == 0:

                del mp[s[start]] 
            
            start +=1
                            
        
        if len(mp) == k:
        
            maxlength = max(maxlength, end-start+1)
    
    print(maxlength)

s = "aabacbebebe"
k = 3

longestKSubstr(s,k)