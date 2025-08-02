class Solution:
    # your task is to complete this function
    # function should return false if length is even
    # else return true
    def isLengthEven(self, head):
        # Code here
        
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