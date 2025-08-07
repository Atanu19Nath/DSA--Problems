
s = "aaaab"

list1 = []
fq = {}
set1 = set()
for i in range(len(s)+1):

    for j in range(i+1,len(s)+1):

        list1.append(s[i:j])
        set1.add(s[i:j])

        if s[i:j] in fq:
            fq[s[i:j]] += 1
        else:
            fq[s[i:j]] = 1

print(list1)
print(set1)

for i in fq:

    print(i,":" ,fq[i])

