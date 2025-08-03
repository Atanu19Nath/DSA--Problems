
# complete this function
# return head of list after swapping
class Solution:    
    def pairWiseSwap(self, head):
        
        if head == None or head.next == None:
            
            return head
            
            
        pre = None
        
        slow = head
        
        fast = head.next
        
        while fast:
            
            next_node = fast.next
            
            if pre == None:
                
                slow.next = next_node
                
                fast.next = slow
                
                head = fast
                
            else:
                
                pre.next =fast
                
                fast.next = slow
                
                slow.next = next_node
                
            
            pre = slow
            
            slow = next_node
            
            if next_node is None:
                break
            
            fast = next_node.next
            
            
            
        return head
                
                
        