def findfloor(arr,x):

    start = 0

    end = len(arr) -1

    ans = -1

    while start <=end:

        mid = start + (end-start)//2

        if arr[mid]<=x:

            ans = mid

            start = mid + 1

        else:

            end = mid -1

    return ans

arr  = [1, 2, 8, 10, 10, 12, 19]
x = 0

print(findfloor(arr,x))