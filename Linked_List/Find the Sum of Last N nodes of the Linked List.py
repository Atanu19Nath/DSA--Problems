'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def sumOfLastN_Nodes(self, head, n):
        #function should return sum of last n nodes
        
        if head == None:
            
            return 0
            
        current = head
        
        total_sum = 0
        list_len = 0
        while current:
            
            total_sum = total_sum + current.data
            list_len +=1
            
            current = current.next
            
        current = head
        
        start_node_sum = 0
        
        check = 0
        while current:
            
            if list_len - n == check:
                
                return total_sum - start_node_sum
            else:
                
                check +=1
                
                start_node_sum = start_node_sum + current.data
                
            current = current.next
            
        
        return 0
            
            
            