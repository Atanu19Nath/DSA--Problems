class Solution:
    def countFreq(self, arr, k):
        # code here
        
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


        first = helper(arr, k, True)
        
        if first == -1:
            
            return 0
            
        last = helper(arr, k, False)
        
        return last - first + 1

        

        
    
            
            
s = Solution()

# arr = [10,20,30,45,50,60,70,80,90,100]
arr = [1 ,3 ,5 ,5 ,5 ,5 ,67 ,123 ,125]

print(arr)

count  = s.countFreq(arr,5)

print(count)




                
                