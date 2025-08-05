'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def joinTheLists(self, head1, head2):
        
        if head1 == None or head2 == None:
            return None
            
        current = head1
        
        while current.next:
            
            current = current.next
            
        
        current.next = head2
        
        
        return head1
            
            