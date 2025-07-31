class Solution:
    # Function to find the maximum product of any two adjacent elements in the array.
    def maxValue(self, arr):
        #code here

        i = 0

        j = len(arr)-1

        maxi = float('-inf')

        while i < j:

            mini = min(arr[i],arr[j])

            ans = abs(i - j) * mini
            maxi = max(maxi,ans)

            if arr[i] < arr[j]:
                i +=1

            elif arr[j]< arr[i]:
                j-=1
                
            elif arr[j] ==arr[i]:
                i+=1
                j-=1

        return maxi

s =Solution()

print(s.maxValue([8, 1, 9, 4]))