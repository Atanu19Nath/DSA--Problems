class Solution:
    def binarysearch(self, arr, k):
        
        start = 0 
        end = len(arr)-1
        ans = -1

        isascending = arr[start] < arr[end]

        
        while start <= end:
                
            mid = start + (end - start) //2

                
            if arr[mid] == k:
                    
                ans = mid
                    
                end = mid -1

            if isascending:
                    
                if k > arr[mid] :
                        
                        start = mid + 1
                        
                else:
                        
                    end = mid -1

            else:

                if k < arr[mid] :
                    
                    start = mid + 1
                    
                else:
                    
                    end = mid -1

        return ans 
            
            
s = Solution()

arr = [10,20,30,45,50,60,70,80,90,100]
arr2 = [100,90,80,70,60,50,40,30,20,10]

print(arr)

print(s.binarysearch(arr,70))

print(arr2)
print(s.binarysearch(arr2,70))

                
                