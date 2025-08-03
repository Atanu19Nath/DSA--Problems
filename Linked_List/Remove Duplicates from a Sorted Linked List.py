
#Function to remove duplicates from sorted linked list.
def removeDuplicates(head):
    #code here
    
    if head == None:
        
        return head
        
    pre = head
    
    next_ele = head.next
    
    while pre and next_ele:
        
        if pre.data == next_ele.data:
            
            while pre.data == next_ele.data:
                
                next_ele = next_ele.next
                
                if next_ele == None:
                    break
            
            if next_ele == None:
                
                pre.next = next_ele
            else:
                
                pre.next = next_ele
            
                pre = pre.next
        
                next_ele = next_ele.next
                
        
        else:
            
            pre = pre.next
        
            next_ele = next_ele.next
        
    return head
        
        