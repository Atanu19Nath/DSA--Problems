class Solution:
    def findFirstNode(self, head):
        #code here
        
        if head == None:
            return head
            
        
        slow = head
        fast = head
        
        check = False
        
        while fast and fast.next:
            
            slow = slow.next
            
            fast = fast.next.next
            
            if slow == fast:     # cycle detedction
                
                slow = head
                
                while slow != fast:  #finding first node in cLL
                    
                    slow = slow.next
                    fast = fast.next
                
                if fast == slow:
                    
                    return slow
            
            
        return None
        
                
                