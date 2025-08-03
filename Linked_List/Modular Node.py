class Solution:
    def modularNode(self, head, k):
        # Code Here
        
        if head == None:
            
            return -1
            
        current = head
        
        maxi = -1
        
        index = 1
        
        ans = {}
        
        while current:
            
            if index % k == 0:
                
                maxi = max(index,maxi)
            
            ans[index] = current.data
            
            index += 1
                
            current = current.next
            
        if maxi == -1:
            return maxi
        else:
            return ans[maxi]