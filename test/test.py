def check(arr):

    start = 0

    end = len(arr) -1

    n = len(arr)

    
    while start <= end :
        
        mid = start + ( end - start )//2

        pre = (mid + n - 1) % n

        next = (mid + 1) % n
        
        print(pre,mid,next)
        
        if arr[mid] < arr[pre] and arr[mid] < arr[next]:
            
            return mid
        
        elif arr[start] <= arr[mid]:
            
            start = mid + 1
            
        else:
            
            end = mid - 1
            
        if arr[0] < arr[n-1]:
            
            return 0
            
    return -1
        
    
    
    
# arr = [7, 9, 11, 12, 5]

# arr = [15, 18, 2, 3, 6, 12]

# arr = [7, 9, 11, 12, 15]

arr = [2,1,3,4]

print(check(arr))
    
