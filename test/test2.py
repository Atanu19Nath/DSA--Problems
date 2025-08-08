class Solution:
    def countSubarrays(self, arr, k):
        # Code here
    
        
        

        count_sa = 0
        for start in range(len(arr)):

            count = 0

            for end in range(start, len(arr)):

                if arr[end]  % 2 != 0:

                    count +=1

                if count == k:

                    count_sa +=1
   
                        
        return count_sa
    

s = Solution()

arr = [2, 2, 5, 6, 9, 2, 11]
k = 2

print(s.countSubarrays(arr,k))