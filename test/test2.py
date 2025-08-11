class Solution:
    def longestOnes(self, arr,k):

        maxlength = 0

        start = 0

        countzero = 0

        for end in range(len(arr)):

            if arr[end] == 0:

                countzero +=1

            if countzero > k:

                if arr[start] == 0:
                     
                    countzero -=1  
                    
                start +=1   

            if countzero == k:    
                maxlength = max(maxlength,end-start+1)
   

        print(maxlength)

# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k = 3

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
s = Solution()

s.longestOnes(nums,k)