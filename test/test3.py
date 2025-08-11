def longestKSubstr(s,k):
    
    maxlength = 0
    for i in range(len(s)):

        set1 = set()

        for j in range(i, len(s)):

            set1.add(s[j])

            if len(set1) > 3:
 
                break
            
            maxlength = max(maxlength, j - i + 1)
            

    
    print(maxlength)



s = "aabacbebebe"
k = 3

longestKSubstr(s,k)