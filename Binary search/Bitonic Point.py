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
			
arr = [1, 2, 4, 5, 7, 8, 3]

print(findBiotonic_point(arr))