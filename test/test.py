def next_greater(arr,x):
    
    start = 0
    
    end = len(arr) -1
    
    ans = -1
    
    while start <= end:
        
        mid = start + ( end - start)//2
        
        print(start, mid ,end)
        
        if arr[mid] == x and mid < len(arr) -1:
            
            ans = arr[mid+1]
            
            start = mid +  1
            
        elif mid > 0 and arr[mid-1] < target  and target < arr[mid]:
            
            ans = arr[mid]
            
            start = mid + 1
            
        elif x > arr[mid]:
            
            start = mid +  1
            
        else:
            
            end = mid -1
            
    if ans == -1:
        
        return arr[0]
    
    elif ans == target:
        
        return arr[0]
    
    else:
        return ans
        

letters = ["e","e","g","g"]

target = "g"

print(letters)


print(next_greater(letters,target))