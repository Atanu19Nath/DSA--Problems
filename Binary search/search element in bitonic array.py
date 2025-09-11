# more correct version

def binary_search_inc(arr,k,start,end):
    
    
    while start <= end:
        
        mid = start + ( end - start )//2
        
        if arr[mid] == k:
            
            return mid

        elif k > arr[mid]:
            
            start = mid + 1
        
        else:
            
            end = mid - 1
            
    return -1
            
            
def binary_search_dec(arr,k,start,end):
    
    
    while start <= end:
        
        mid = start + ( end - start )//2
        
        if arr[mid] == k:
            
            return mid

        elif k < arr[mid]:
            
            start = mid + 1
            
        else:
             end = mid - 1
            
            
    return -1
        
    
            
def search_element_Biotonic_array(arr,k):
    
    size = len(arr)
    
    
    
    if size == 1:
        
        if arr[0] == k:
        
            return 0
        
        else:
            
            return -1
    
    if arr[0] == k:
        
        return 0
    
    if arr[size -1 ] == k:
        
        return size-1
    
    
    start = 1
    
    end = size - 2
    
    while start <=end:
        
        mid = start + ( end - start )//2
        if arr[mid] == k:
            
            return mid 
        
        if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
            
            ans1 = binary_search_inc(arr,k,0,mid-1)
            
            if ans1 != -1:
                
                return ans1
            ans2 = binary_search_dec(arr,k,mid,size-1)
            
            if ans2 != -1:
                
                return ans2
            
    
        
        elif arr[mid] < arr[mid+1]:
            
            start = mid + 1
            
        else:
            
            end = mid - 1
            
    
    return -1
            

			
arr = [1, 3,8,12,4,2]

print(search_element_Biotonic_array(arr,4))