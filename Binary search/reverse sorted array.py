class Solution:
    def binarysearch(self, arr, k):

        start = 0

        end = len(arr) -1

        ans = -1

        while start <= end:

            mid = start + (end-start)//2

            if arr[mid] == k:

                ans = mid

                end = mid - 1

            elif k < arr[mid]:

                start = mid + 1

            else:

                end = mid -1

        
        return ans
       
            
            
s = Solution()


arr2 = [100,90,80,70,60,50,40,30,20,10]

print(s.binarysearch(arr2,70))

                
                