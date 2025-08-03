#Your task is to complete this function
#Your function should return the new head pointer
'''
class node:
    def __init__(self,x):
        self.data = x
        self.next = None
'''

class Solution:
    def deleteK(self, head, k):
        #code here  
        
        if head == None or k == 1:
            
            print(-1)
            
            return None
        
        
        pre = None
        
        current = head
        
        count = 1
        
        while current:
            
            if k == count:
                new_node = current.next
                current.next = None
                pre.next = new_node
                
                if new_node == None:
                    break
                current = new_node
                count = 1
            else:
                pre = current
                current = current.next
                count +=1
               
               
        return head 
                