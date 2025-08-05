#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def deleteAtPosition(head, pos):
    #code here
    
    if head == None:
        
        return head
    
    current = head
    
    pre = head
    
    current = head.next
    
    check = 2
    
    if pos == 1:
        
        head.next = None
        
        head = current
        
        return head
    
    while current:
        
        if check == pos:
            
            pre.next = current.next
            
            current.next = None
            
            return head
        
        check +=1
        pre = current    
        current = current.next
        
    
        
    
        
        
    return head