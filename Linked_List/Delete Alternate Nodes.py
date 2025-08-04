class Solution:
    def deleteAlt(self, head):
        # code here
        
        if head == None:
            
            return head
            
        
        pre = None
        
        current = head
        
        k = 2
        
        count = 1
        
        while current:
            
            if pre == None:
                
                pre = current
                
                current = current.next
                
                count +=1
                
            elif count == k :
                
                new_node = current.next
                
                pre.next = new_node
                
                current = new_node
                
                count = 1
                
            elif count != k:
                
                pre = current
                
                current = current.next
                
                count +=1
                
                
            
        return head
                
                
                
                
            