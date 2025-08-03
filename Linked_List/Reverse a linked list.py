class Solution:
    def reverseList(self, head):
        # Code here
        if head == None:
            
            return head
            
        pre = None
        current = head
        
        while current:
            
            next_node = current.next
            current.next = pre
            pre = current
            current = next_node
            
        
        head = pre
        
        return head