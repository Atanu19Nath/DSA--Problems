arr = [10,20,30,45,50,60,70,80,90,100]


mid = 5

n = len(arr)

print(mid + 1)

print(mid + n - 1)


next = (mid + 1) % n
pre = (mid + n - 1) % n

print("pre = ",pre,"next = ",next)