class Solution:
	def immediateSmaller(self, arr):
		
		for i in range(0,len(arr)-1):
			
			if arr[i+1] < arr[i]:
				arr[i] = arr[i+1]
			elif arr[i+1] >= arr[i]:
				arr[i] = -1
		       
		        
		arr[len(arr) - 1] = -1
		return arr
	
s = Solution()

print(s.immediateSmaller([4, 2, 1, 5, 3]))
		      