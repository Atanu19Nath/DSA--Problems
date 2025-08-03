
class Solution:

    def deleteMid(self, head):
        '''
        head:  head of given linkedList
        return: head of resultant llist
        '''

        #code here
        if head is None or head.next is None:
            
            return None
            
        pre = None
        
        slow = head
        
        fast = head
        
        
        while fast and fast.next:
            
            
            pre = slow
            
            slow = slow.next
            
            fast = fast.next.next
            
            
        pre.next = slow.next
        
        slow.next = None
        
        
            
        
        return head
            
            
            