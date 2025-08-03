'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self,head):
        #Your code here
        
        if head == None:
            return head
            
        current = head
        
        stack = []
        
        stack.append(current.data)
        
        current = current.next
    
        while current:
            
            if current.data > stack[len(stack) -1]:
                
                while len(stack) and current.data > stack[len(stack) -1]:
                    
                    stack.pop()
                
            stack.append(current.data)
            
            current = current.next
            
            
        stack.reverse()
        head2 = None
        
        for i in stack:
            
            new_node = Node(i)
            
            if head == None:
                
                head2 = new_node
                
            else:
                
                new_node.next = head2
                
                head2 = new_node
                
        
        
        
        return head2
            
            
                
            
                