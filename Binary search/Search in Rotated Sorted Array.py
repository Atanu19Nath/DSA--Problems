def count_rotation2(arr,k):

    start = 0

    end = len(arr) -1

    ans = -1


    while start <=end:

        mid = start + ( end - start )//2

        if arr[mid] == k :

            return mid

        elif arr[mid] > arr[end]:

            if k < arr[mid] :

                end = mid
            else:
                start = mid

        else:

            start = mid +1 

    
    return ans


# arr = [15, 18, 20, 30, 40, 5, 6, 7]

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]

print(count_rotation2(arr,10))