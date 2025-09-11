def findBiotonic_point(arr):
	
    start = 0
	
    end = len(arr) -1
	
    n = len(arr)
    
    while start<=end:
        
        mid = start + ( end - start )//2
        
        next = ( mid + 1) % n
        
        pre = ( mid + n - 1) % n
        
        if arr[pre] < arr[mid] > arr[next]:
            
            return arr[mid]
		
        elif arr[mid] < arr[next]:
            
            start = mid + 1
            
        else:
            
            end = mid - 1
            
            
# more correct version
            
def findBiotonic_point2(arr):
    
    size = len(arr)
    
    if size == 1 or arr[0] > arr[1]:
        
        return arr[0]
    
    if arr[size -1 ] > arr[size -2]:
        
        return arr[size-1]
    
    
    start = 1
    
    end = size - 2
    
    while start <=end:
        
        mid = start + ( end - start )//2
        
        if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
            
            return arr[mid]
        
        elif arr[mid] < arr[mid+1]:
            
            start = mid + 1
            
        else:
            
            end = mid - 1
            
        
            

			
arr = [1, 2, 4, 5, 7, 8, 3]

print(findBiotonic_point(arr))

print(findBiotonic_point2(arr))