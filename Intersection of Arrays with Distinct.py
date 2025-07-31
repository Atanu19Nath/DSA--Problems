class Solution:
    def intersectSize(self,a, b):

        a.sort()
        b.sort()

        i = 0
        j = 0
        count = 0
        while i < len(a) and j < len(b):

            if a[i] < b[j]:
                i +=1
            elif a[i] > b[j]:
                j +=1
            
            elif a[i] == b[j]:
                count +=1
                i +=1
                j +=1

        return count

s = Solution()

print(s.intersectSize([89, 24, 75, 11, 23],[89, 2, 4]))