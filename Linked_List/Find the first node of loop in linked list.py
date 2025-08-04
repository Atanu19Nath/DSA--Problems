#User function Template for python3

""" Node Class
    class Node:
        def __init__(self, data):   # data -> value stored in node
            self.data = data
            self.next = None
"""
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
        
                
                