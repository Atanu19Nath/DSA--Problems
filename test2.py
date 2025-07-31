from collections import Counter

arr= [1,3,2,3,4]


ans = Counter(arr)

print(ans)

for i in range(len(ans)):

    if ans[arr[i]] > 1:

        print(arr[i])
        break