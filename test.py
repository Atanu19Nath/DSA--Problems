class Solution:
    def maxLen(self, arr):
        prefix_sum = 0
        maxi = 0
        seen = {}

        for i in range(len(arr)):
            # Replace 0 with -1
            if arr[i] == 0:
                arr[i] = -1

        print(arr)

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum == 0:
                max_len = i + 1

            if prefix_sum in seen:
                max_len = max(max_len, i - seen[prefix_sum])
            else:
                seen[prefix_sum] = i

        print(seen)
        return maxi
s = Solution()

arr = [1, 0, 1, 1, 1, 0, 0]

print(s.maxLen(arr))