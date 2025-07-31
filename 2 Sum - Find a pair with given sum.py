#User function Template for python3
class Solution:
    # Complete the below function
    def twoSum(self,arr, target):
        # Your code here
        
        arr.sort()
        
        i = 0
        j = len(arr)-1
        
        while i < j:
            
            sum = arr[i] + arr[j]
            
            if sum > target:
                
                j -= 1
            elif sum < target:
                
                i +=1
                
            elif sum == target:
                
                return [arr[i],arr[j]]
        
        
        return []
    

s = Solution()

print(s.twoSum([2, 9, 10, 4, 15],12))