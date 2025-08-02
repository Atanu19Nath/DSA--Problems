class Solution:
    def celebrity(self, arr):
        # code here

        if len(arr) == 1:

            return 0
        
        list = {}

        print(arr)

        for i in range(0,len(arr)):

            list[i] = 1

            for j in range(0,len(arr[i])):

                if j != i and arr[i][j] == 1:
                    list[i] = list[i] + 1
            


        print(list) 
          
        for i in list:

            print(i, list[i])


        for i in list:

        
            if list[i] == 1:

               return i

        
        return -1    

s = Solution()

arr = [
    [1, 1, 1],
    [0, 1, 0],
    [1, 0, 1]
]

print(s.celebrity(arr))
