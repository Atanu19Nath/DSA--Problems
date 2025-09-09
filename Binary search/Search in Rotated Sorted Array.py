def search(arr,k):

    start = 0

    end = len(arr) -1

    n = len(arr)

    while start <= end:

        mid = start + (end - start) //2

        print("start = ",start ," end = ", end, "mid = ",mid)

        if arr[mid] == k:

            return mid

        elif arr[start] <= arr[mid]:

            if arr[start] <= k < arr[mid]:

                end = mid -1

            else:

                start = mid + 1

        else:

            if arr[mid] < k  <= arr[end] :

                start = mid + 1

            else: 

                end = mid -1


    return -1


# arr = [15, 18, 20, 30, 40, 5, 6, 7]

# arr = [1,2,3,5,6,7,8,9,10]

arr = [15, 18, 20, 30, 40, 5, 6, 7]

print(search(arr,6))