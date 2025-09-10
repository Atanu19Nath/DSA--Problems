def find_minimum_element(arr,x):


    start = 0

    end = len(arr) -1

    mini = float('inf')

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

    return ans 

def find_minimum_element2(arr,x):

    start = 0

    end = len(arr) -1

    mini = float('inf')

    while start <= end:

        mid = start + ( end - start )//2

        if arr[mid] == x :

            return arr[mid]

        if x > arr[mid]:

            start = mid + 1

        else:

            end = mid - 1

     # handle edge cases

    if start >= len(arr):   # x is bigger than all elements

        return arr[end]
    
    if end < 0:             # x is smaller than all elements
        
        return arr[start]
    
    
    ans1 = abs(arr[start] - x)
    ans2 = abs(arr[end] - x)

    if ans1 < ans2:

        return arr[start]
    
    elif ans2 < ans1:

        return arr[end]
    
    else:

        return max(arr[start], arr[end])

        

arr = [1,3,8,10,15]

x = 20

print(find_minimum_element(arr,x))
print(find_minimum_element2(arr,x))