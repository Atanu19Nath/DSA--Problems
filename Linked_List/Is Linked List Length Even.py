class Solution:
    def isLengthEven(self, head):
        
        
        if head == None:
            
            return False
            
        current = head
        count = 0
        
        while current:
            
            count +=1
            
            current = current.next
            
        
        if count % 2 == 0:
            
            return True
        
        return False