def findCeil(arr, x):
        
        start = 0
        
        end = len(arr) -1
        
        ans = -1
        
        while start <= end:
            
            mid = start + (end - start)//2
            
            if arr[mid] >= x :
                
                ans = mid
                
                end = mid - 1
                
            else:
                
                start = mid + 1
                
        return ans

arr = [1, 2, 8, 10, 11, 12, 19]

x = 5

print(findCeil(arr,x))