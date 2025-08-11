class Solution:
    def longestOnes(self, arr,k):

        maxlength = 0

        for i in range(len(arr)):
     
            countzero = 0

            if arr[i]  == 0:

                countzero +=1
                
            for j in range(i+1,len(arr)):

                if arr[j] == 0:

                    countzero +=1
                    
                if countzero == k:

                    maxlength = max(maxlength,j-i+1)
   

        print(maxlength)
        
arr = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
s = Solution()

s.longestOnes(arr,k)