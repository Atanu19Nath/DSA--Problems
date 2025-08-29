class Solution:
    def dailyTemperatures(self, arr):

        stack = []

        index = {}

        n = len(arr)

        if arr:

            stack.append(arr[-1])
            index[arr[-1]] = n -1
            arr[-1] = 0
            
        
        for i in range(n-2,-1,-1):

            val = arr[i]

            while stack and val >= stack[-1]:

                del index[stack[-1]]

                stack.pop()
                
            
            if len(stack) == 0:

                arr[i] = 0

            else:

                arr[i] = index[stack[-1]] - i

            stack.append(val)

            index[val] = i

        return arr


s = Solution()

# temperatures = [73,74,75,71,69,72,76,73]

temperatures = [89,62,70,58,47,47,46,76,100,70]

print(s.dailyTemperatures(temperatures))