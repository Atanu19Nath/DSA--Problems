'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

''' your task is to complete this function
    function should return a list of the two new heads
'''
class Solution:
    def merge_list(self, head1, head2):
        # code here
        if head1 == None or head2 == None:
            
            return head1.head2
            
        
        if head1.next == None:
            
            current2 = head2
            
            head1.next = current2
            
            head2 = current2.next
            
            current2.next = None
            
            return head1,head2
            
        c1 = head1.next
        
        p1 = head1
        
        c2 = head2.next
        
        p2 = head2
        
        while c1:
            
            if c2 == None and c1:
            
                p1.next = p2
                p2.next = c1
                
                head2 = None
                
                break
            
            p1.next = p2
            p2.next = c1
            p1 = c1
            c1 = c1.next
            
            head2 = c2
            p2 = c2
            c2 = c2.next
        
        if c1 == None and c2:
            
            p1.next = p2
            p2.next = None
            head2 = c2
        
        if c1 == None and c2 == None:
            
            p1.next = p2
            p2.next = None
            head2 = None
            
            
        return head1,head2
        
            
            