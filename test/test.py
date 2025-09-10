def find_minimum_element(arr,x):


    start = 0

    end = len(arr) -1

    mini = float('inf')

    ans = -1

    while start <= end:

        mid = start + ( end - start )//2

        if arr[mid] == x :

            return arr[mid]
        
        diff = abs(arr[mid] - x)

        if diff < mini or (diff == mini and ans < arr[mid]):

            mini = diff

            ans = arr[mid]

        if x > arr[mid]:

            start = mid + 1

        else:

            end = mid - 1

    
    print(arr[start],arr[end])

    return ans 
        


        

arr = [1,3,8,11,15]

x = 12

print(find_minimum_element(arr,x))