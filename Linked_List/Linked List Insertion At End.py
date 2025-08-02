# '''    
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# '''
class Solution:
    def insertAtEnd(self, head, x):
        
        #code here
        if head == None:
            
            new_node = Node(x)
            
            head = new_node
            
            return head
        
        current = head
        
        while current.next:
                
            current = current.next
               
        new_node = Node(x)
                
        current.next = new_node
      
        
        return head