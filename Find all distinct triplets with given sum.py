#User function Template for python3
class Solution:
    def threeSum(self, arr, target):
        # Your code here
        
        if len(arr) < 3:

            return []
         
        arr.sort()

        i = 0
        j = len(arr) -1
        k = len(arr) -2

        lista = []
            
        for i in range(len(arr)):

            k = i + 1
            j = len(arr) -1

            sum = arr[i]

            while( k < j):

                sum = arr[i] + arr[k] + arr[j]

                if sum < target:

                    k +=1
                elif sum > target:

                    j -=1

                elif sum == target:

                    lista.append([arr[i],arr[k],arr[j]])
                    k +=1
                    j-=1


        #convert list item to tuple then add in final list .

        check = set()
        visited = []
        for i in lista:

            tup = tuple(i)

            if tup not in check:
                check.add(tup)
                visited.append(list(tup))
                
        
        return visited


                


        

s = Solution()

arr = [78,78,0,4427,0,0,0]
target = 78

print(s.threeSum(arr,target))