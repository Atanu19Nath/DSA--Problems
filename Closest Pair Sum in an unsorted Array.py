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
numbers = [
    6722, 6186, 3414, 1930, 1274, 4188, 9817, 8555, 6653, 3845, 7851, 4446, 3426, 1548, 5973,
    1771, 5753, 9763, 1798, 5107, 5293, 5770, 3500, 8249, 1631, 3119, 2595, 2198, 3420, 2393,
    8947, 141, 9658, 3440, 3150, 931, 7628, 4046, 9486, 5359, 7891, 8416, 9805, 1316, 9964,
    5777, 4166, 6795, 5539, 7044, 1901, 832, 2813, 6480, 159, 5523, 677, 2754, 7721, 4098,
    6226, 7747, 5318, 5883, 1186, 9548, 7894, 9893, 3593, 7379, 5251, 1483, 6873, 5055, 3879,
    7915, 1910, 9124, 5788, 8529, 6167, 8769, 439, 8980
]

print("solution",s.closestPairSum(numbers,8139))