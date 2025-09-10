def next_alph(arr,x):

    start = 0

    end = len(arr) -1

    n = len(arr)

    while start <= end:

        mid = start + (end - start) //2

        next = (mid + 1) % n
    
        print("mid = ",mid,"next = ",next)


        if arr[mid] == x:

            return next
        
        elif x > arr[mid]:

            start = mid + 1

        else:

            end = mid -1

    return -1



# arr = [15, 18, 20, 30, 40, 5, 6, 7]

arr = ["a","c","f","h"]

print(next_alph(arr,'m'))