
class Solution:
    def count(self, head, key):
        # Code here
        
        if head == None:
            
            return 0
            
        current = head
        
        count = 0
        
        while current:
            
            if key == current.data:
                
                count +=1
                
            current = current.next
        
        return count
        
            
            