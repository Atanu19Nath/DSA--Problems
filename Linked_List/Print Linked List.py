class Solution:
    # Function to display the elements of a linked list in same line
    def printList(self, head):
        #code here
        
        if head == None:
            
            return head
        
        current = head
        
        while current:
            
            print(current.data, end=" ")
            
            current = current.next