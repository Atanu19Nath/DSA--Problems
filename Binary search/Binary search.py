class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        
        
        i = 0 
        j = len(arr)-1
        ans = -1
        
        while i <= j:
            
            mid = i + (j - i) //2

            print ("mid = ",mid)
            
            if arr[mid] == k:
                
                ans = mid
                
                j = mid -1
                
            elif k > arr[mid] :
                
                i = mid + 1
                
            else:
                
                j = mid -1
            
        
        return ans 
    
    def binarysearch_rec(self,arr,k):

        def helper(arr,k,left,right):

            if left<=right:

                mid = left + (right - left) // 2

                if arr[mid] == k:
                    
                    left_result = helper(arr, k, left, mid - 1)

                    return mid if left_result == -1 else left_result

                elif k > arr[mid]:

                    return helper(arr,k,mid+1,right)
                
                else:

                    return helper(arr,k,left,mid-1)
                
            else:

                return -1
        
        left = 0

        right = len(arr) -1

        ans =  helper(arr,k,0,len(arr)-1)

        print("my ans is =",ans)

        return ans

                
            
            
s = Solution()

arr = [10,20,30,45,50,60,70,80,90,100]

print(s.binarysearch(arr,70))

print(s.binarysearch_rec(arr,70))
                
                