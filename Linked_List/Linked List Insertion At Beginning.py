#User function Template for python3

class Solution:
    # Function to insert a node at the beginning of the linked list
    def insertAtBegining(self, head, x):
        # Code here
        
        if head == None:
            
            return head
        
            
        new_node = Node(x)
            
        new_node.next = head
            
        head = new_node
        
        return head