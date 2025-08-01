from typing import List
class Solution:
    def pairsum(self, arr : List[int]) -> int:
        # code here

        arr.sort()

        i = 0
        j = len(arr) - 1

        maxi = float('-inf')

        while i < j:

            if arr[i] != arr[j]:

                sum = arr[i] + arr[j]

                maxi = max(maxi,sum)
            
            i +=1
        
        return maxi


s = Solution()

arr = [12, 34, 10, 6, 40]

print(s.pairsum(arr))
        
