arr = [10,20,30,45,50,60,70,80,90,100]


low = 0

high = len(arr) -1

mid = low + (high-low)//2

print(arr[mid])

print(arr[:mid])

print(arr[mid+1:])