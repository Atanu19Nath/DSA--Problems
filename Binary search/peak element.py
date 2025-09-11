def peakElement(arr):
        
        size = len(arr)

        # for only one element

        if size == 1:
    
            return 0
    
        # check first element peak or not
    
        if arr[0] > arr[1]:
    
            return 0
        
        # check last lement peak or not
    
        if arr[size - 1] > arr[size -2] :
    
            return size -1
    
        start = 1
    
        end = size - 2
    
        while start <= end:
    
            mid = start + ( end - start )//2
           
    
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
    
                return mid
                
            if arr[mid] < arr[mid +1 ]:
    
                start = mid + 1 
    
            else:
    
                end = mid - 1
    
        return 0

arr = [1, 2, 4, 5, 7, 8, 3]

print(peakElement(arr))