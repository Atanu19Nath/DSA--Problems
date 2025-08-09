class Solution:
    def minRemovals(self, arr, k):
        # code here
        
        lsum = 0
        rsum = 0
        mincount = 0
        
        i = 0

        size = len(arr) -1

        while lsum < k and i < size:
            
            lsum = lsum + arr[i]

            i +=1

        if lsum == k:

            mincount = i


        r = size -1 

        s = i -1

        while lsum > 0:


            rsum = rsum + arr[r]

            while lsum + rsum > k:

                lsum = lsum - arr[s]

                s-=1 

            
            if lsum + rsum == k:
                
                mincount = min(mincount, i+1+size-r+1)

            r -=1

        return mincount
            
            
            
            
s = Solution()

arr = [6, 3 ,1 ,2 ,10, 10]
k = 20
print(s.minRemovals(arr,k))