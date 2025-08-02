#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def searchLinkedList(self, head, x):
        #code here
        
        if head == None:
            
            return 0
            
        current = head 
        
        while current:
            
            if x == current.data:
                
                return True
                
            current = current.next
        
        return False