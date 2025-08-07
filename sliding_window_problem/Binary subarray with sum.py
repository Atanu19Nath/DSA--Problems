class Solution:
    def numberOfSubarrays(self, arr, target):
        mp = {}
        c_sum = 0
        count = 0

        mp[0] = 1  # This is to handle subarrays starting from index 0

        for j in range(len(arr)):
            c_sum = c_sum + arr[j]

            if (c_sum - target) in mp:
                count = count + mp[c_sum - target]

            if c_sum in mp:
                mp[c_sum] = mp[c_sum] + 1
            else:
                mp[c_sum] = 1

        return count


s = Solution()
arr = [1, 0, 1, 0, 1]
print(s.numberOfSubarrays(arr, 2))  # Output: 4


















# BRUT FORCE O(N2)

# class Solution:
#     def numberOfSubarrays(self, arr, target):
#         # code here
        
#         count = 0
        
#         for i in range(len(arr)):
        
#             c_sum = arr[i]
            
#             if c_sum == target:
                
#                 count +=1
            
#             for j in range(i+1,len(arr)):
        
#                 c_sum = c_sum + arr[j]
                
                
#                 if c_sum == target:
        
#                     count += 1
                    
                    
#         return count
                    
    
            