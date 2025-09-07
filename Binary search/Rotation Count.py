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

             



arr = [15, 18, 20, 30, 40, 50, 60, 3]

print(count_rotation(arr))

print(count_rotation2(arr))