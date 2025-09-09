def count_rotation(arr):


    start = 0

    end = len(arr) - 1

    count = 0

    while arr[start] > arr[end]:

        count +=1
        start +=1

    return count

def count_rotation2(arr):

    start = 0

    end = len(arr) -1


    while start <=end:

        if arr[start] <= arr[end]:

            return start

        mid = start + (end - start)//2

        if arr[mid] > arr[end]:

            start = mid + 1

        else:

            end = mid  

    
    return start

def count_rotation3(arr):

    start = 0

    end = len(arr) -1

    n = len(arr)

    while start <= end:

        mid = start + (end - start) //2

        next = (mid + 1) % n
        pre = (mid + n - 1) % n

        print("mid = ",mid, "pre = ",pre,"next = ",next)


        if arr[mid] <= arr[pre] and arr[mid] <= arr[next]:

            return mid
        
        elif arr[start] <= arr[mid]:


            start = mid + 1

        elif arr[mid] <= arr[end]:

            end = mid -1

    return -1



# arr = [15, 18, 20, 30, 40, 5, 6, 7]

arr = [25,5, 6, 7, 8, 9, 10, 11, 12,13,14]

print(count_rotation(arr))

print(count_rotation2(arr))

print(count_rotation3(arr))