''' structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

class Solution:
    def findIntersection(self,head1,head2):
        #return head
        
        if head1 == None or head2 == None:
            
            return head1
            
        current = head1
        
        list1 = []
        list2 = []
        list3 = []
        
        while current:
            
            list1.append(current.data)
            current = current.next
            
        current = head2
        
        while current:
            list2.append(current.data)
            current = current.next
            
        for i in list1:
            
            if i in list2:
                list3.append(i)
                
                
        # print(list3)
        
        
        head3 = None
        
        list3.reverse()
        for i in list3:
            
            new_node = Node(i)
            if head3 == None:
                
                head3 = new_node
            else:
                
                new_node.next = head3
                
                head3 = new_node
                
        
        return head3
                
                
            