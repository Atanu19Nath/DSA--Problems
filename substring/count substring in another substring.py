
def count_substring(s1,s2):

    count = 0
    set1 = set()
    for i in range(len(s1)):

        for j in range(i+1, len(s1)+1):
            
            sub = s1[i:j]
            if sub in s2  and sub not in set1:

                # print("ok : ",s2[i:j])
                count +=1
                set1.add(sub)
    
    print("count = ",count)


s1 = "aab"
s2 = "aaaab"

count_substring(s1,s2)