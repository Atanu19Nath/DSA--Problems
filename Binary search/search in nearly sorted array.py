def binarysearch(arr, k):
        # Code Here
        
        
        start = 0 
        end = len(arr)-1
        ans = -1
        
        while start <= end:
            
            mid = start + (end - start) //2

            print ("start = ", start, "mid = ",mid, "end = ",end)
            
            if k == arr[mid] :
                
                return mid
            
            elif mid + 1 <= end and k == arr[mid+1]:
                    
                return mid+1
            
            elif mid - 1 >= start and k == arr[mid-1]:
                 
                return mid-1
                
                
            elif k > arr[mid + 1] :
                
                start = mid + 2
                
            else:
                
                end = mid - 2
            
        
        return ans  


arr =  [10, 3, 40, 20, 50, 80, 70]

target = 80

print(arr)

print(binarysearch(arr,target))