class Solution:
    def binarysearch(self, arr, k):
        # Code Here


        def helper(arr,k,check):

            start = 0

            end = len(arr) -1

            ans = -1


            while start <= end:


                mid = start + (end - start)//2

                if arr[mid] == k:

                    ans = mid


                    if check:

                        end = mid - 1
                        
                    else:

                        start = mid + 1

                elif k > arr[mid]:

                    start = mid + 1

                else :

                    end = mid - 1
            
            return ans


        first = helper(arr,k,True)

        last = helper(arr,k,False)

        return first,last


        
    
            
            
s = Solution()

# arr = [10,20,30,45,50,60,70,80,90,100]
arr = [1 ,3 ,5 ,5 ,5 ,5 ,67 ,123 ,125]

print(arr)

first,last  = s.binarysearch(arr,5)



print("first occurance = ",first)
print("last occurance = ",last)


                
                