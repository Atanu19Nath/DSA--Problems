s1 = "geeksforgeeks"
s2 = "geeksquiz"

set1 = set(s1)
set2 = set(s2)
s = ""
for i in set1:
            
    if i not in s2:
                
        s = s + i
                
for i in set2:
            
    if i not in s1:
                
        s = s + i


print(s)