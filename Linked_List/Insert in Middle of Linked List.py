'''
    Your task is to insert a new node in 
	the middle of the linked list with
	the given value.
	
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
	
	Function Arguments: head (head of linked list), node 
	(node to be inserted in middle)
	Return Type: None, just insert the new node at mid.
'''
#Function to insert a node in the middle of the linked list.
class Solution:
    def insertInMiddle(self, head, x):
        #code here
        
        if head == None:
            
            new_node = Node(x)
            
            head = new_node
            
            return head
            
        stack = []
        
        current = head
        
        while current:
            
            stack.append(current)
            
            current = current.next
            
        
        size = len(stack)
        
        if size % 2 == 0:
            
            mid = int(size/2)-1
            
        else:
            
            mid = int(size/2)
            
        
        mid_node = stack[mid]
        
        new_node = Node(x)
        
        next_node = mid_node.next
        
        mid_node.next = new_node
        
        new_node.next = next_node
        
        
        return head
        
        