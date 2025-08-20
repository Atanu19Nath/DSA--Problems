class Solution:
    def countSubArrayProductLessThanK(self, arr, n, k):
        if k <= 1:
            return 0
        
        product = 1
        count = 0
        start = 0

        for end in range(n):
            product *= arr[end]

            while product >= k and start <= end:
                product /= arr[start]
                start += 1

            count += end - start + 1

        return count
