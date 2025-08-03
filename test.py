l = [5 ,2 ,4 ,2]


s = set()
result = []
for i in l:

    if i not in s:
        result.append(i)
        s.add(i)

print(result)