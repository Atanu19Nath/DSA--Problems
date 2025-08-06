#User function Template for python3
class Solution:
    # Function to find a continuous sub-array which adds up to a given number.
    def subarray_sum(self, arr, sum):
        # Your code here
        
        
        c_sum = 0
        
        mp = {}
        
        list1 = []
        for i in range(len(arr)):
            
            c_sum = c_sum + arr[i]
            
            if c_sum == sum :
                
                list1.append(1)
                list1.append(i+1)
                return list1
                
            if c_sum - sum in mp:
                
                list1.append(mp[c_sum-sum]+2)
                
                list1.append(i+1)
                
                return list1
                
            if c_sum - sum not in mp:
                
                mp[c_sum] = i
                
        
        
        if len(list1) == 0:
                
                return -1 
        else:
            
                return list1  

s = Solution()

print(s.subarray_sum([26 ,3 ,28, 7],52))
                    
                