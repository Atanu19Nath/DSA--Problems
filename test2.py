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

        print(count)

s = Solution ()

s.intersectSize([1,2,4,3,5,6],[3,4,5,6,7])