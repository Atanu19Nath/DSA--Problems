#User function Template for python3

class Solution:
    #Complete the below function
    def closestPairSum(self,arr, target):
        #Your code here
        
        arr.sort()
        ans_list = {}
        
        i = 0
        j = len(arr) -1 
        
        while i < j:
            
            sum = arr[i] + arr[j]
            
            diff = abs(target - sum)
            
            if sum < target:
                
                if diff not in ans_list:
                    ans_list[diff] = [arr[i],arr[j]]
                
                i +=1
            elif sum > target:
                
                if diff not in ans_list:
                    ans_list[diff] = [arr[i],arr[j]]
                
                j -=1
            elif sum == target:
                
                return [arr[i],arr[j]]
        
        if len(ans_list) == 0:
            return []
        else:
            return ans_list[min(ans_list.keys())]
                

s = Solution()

print(s.closestPairSum([40, 10, 29, 28, 22, 1, 30],54))