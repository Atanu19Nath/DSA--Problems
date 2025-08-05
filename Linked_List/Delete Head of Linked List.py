
def deleteHead(head):
    #code here
    
    if head == None:
        
        return head
        
        
    new_node = head.next
    
    head.next = None
    
    head = new_node
    
    return head