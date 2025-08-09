class Solution:
    def minRemovals(self, arr, k):
        # code here
        
        tsum = 0
        for i in range(len(arr)):

            tsum = tsum + arr[i]

        target = tsum - k

        if target == 0:
             
            return len(arr)

        start = 0

        length = 0
        
        csum = 0

        size = len(arr)

        for end in range(len(arr)):

            csum = csum + arr[end]

            while csum > target:

                csum = csum - arr[start]

                start +=1

            if csum == target :

                length = max(length,end -start + 1)
        


        print(length)

        if length == 0:
            return -1
        else:
            return size - length





            
s = Solution()
arr = [
    8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000,
    9999, 9993, 9904, 8819, 1231, 6309, 
]

k = 134365

# arr = [5, 3, 4, 6, 2]
# k = 6

print(s.minRemovals(arr,k))