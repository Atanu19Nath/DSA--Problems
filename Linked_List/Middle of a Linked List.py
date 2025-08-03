class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def getMiddle(self, head):
        # Code here
        # return the value stored in the middle node
        
        if head == None:
            
            return head
            
        slow = head 
        fast = head
        
        while fast and fast.next:
            
            fast = fast.next.next
            
            slow = slow.next
            
            
        
        return slow.data