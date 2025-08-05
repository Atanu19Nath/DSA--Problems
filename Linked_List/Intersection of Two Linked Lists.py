''' structure of list node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

class Solution:
    def findIntersection(self, head1, head2):
        # code here
        
        if head1 == None or head2 ==None:
            
            return None
            
        set1 = set()
        
        list2 = []
        
        current = head2
        
        while current:
            
            set1.add(current.data)
            
            current = current.next
            
            
            
        current = head1
    
        while current:
            
            if current.data in set1:
                
                list2.append(current.data)
            
            current = current.next
            
            
        # print(list2)
        
        head3 = None 
        
        for i in list2:
            
            new_node = Node(i)
            
            if head3 == None:
                
                head3 = new_node
                tail = new_node
            
            else:
                
                tail.next = new_node
                
                tail = new_node
                
        
        return head3
                
                
            
            