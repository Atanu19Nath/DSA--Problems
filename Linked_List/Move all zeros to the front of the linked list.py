class Solution:
    def moveZeroes(self, head):
        #code here
        
        if head == None:
            
            return head
            
        p = None
        c = head
        
        if c.data == 0 :
            
            p = head.next
            c = p.next
        else:
            
            p = c
            c = c.next
            
        while c :
            
            if c.data == 0:
                p.next = c.next 
                c.next = head
            
                head = c
                c = p.next
            
            else:
                
                p = c
                c = c.next

        
        return head
            
        