# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def deleteNode(head, x):
    # Code here
    
    if head == None:
        
        return head
        
    slow = head
    fast = head.next
    
    
    if x == 1:
        
        head = fast
        
        return head
    
    count = 2
    
    while fast:
        
        if count == x:
            
            slow.next = fast.next
        
        count +=1
        slow = slow.next
        fast = fast.next
        
    
    return head
    
    