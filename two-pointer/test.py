class Solution:
    def nextLargerElement(self, arr):
        # code here

        i = 0
        ans = []
        stack = []
        size = len(arr)

        while i < size - 1:

            if arr[i] < arr[i + 1]:
                
                if len(stack) != 0:

                    Check = stack[len(stack)-1]

                    print("check1:",Check)
                    
                    while arr[i+1] > arr[Check] :
                        ans[Check]= arr[i+1]
    
                        stack.pop()

                        if len(stack) != 0:
                            Check = stack[len(stack)-1]
                            print("check2=",Check)
                        else:
                            break    
                            
                
                ans.append(arr[i+1])
                

            elif arr[i] >= arr[i +1]:

                stack.append(i)
                ans.append(0)

            i +=1
        
        while len(stack) != 0:

            pos = stack.pop()
           

            ans[pos] = -1
        
        ans.append(-1)
        
        return ans
    

s = Solution()

print(s.nextLargerElement([6,8,8,0,1,9]))