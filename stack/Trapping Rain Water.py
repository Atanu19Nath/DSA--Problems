
class Solution:
    def maxWater(self, arr):
        # code here

        left = []
        right = []
        size = len(arr)
        maxl = arr[0]
        left.append(maxl)

        for i in range(1,len(arr)):
            if arr[i] > maxl:
                maxl = arr[i]
            left.append(maxl)
        

        maxr = arr[size - 1]
        right.append(maxr)

        for j in range(size - 2,-1,-1):
    
            if arr[j] > maxr:
                maxr = arr[j]
            right.append(maxr)

        right.reverse()

        sum = 0
        for k in range(0,size-1):
            
            result = min(left[k],right[k]) - arr[k]
            sum = sum + result
        
        return sum




        

s = Solution()

print(s.maxWater([3,0,1,0,4,0,2]))
