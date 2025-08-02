'''
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
'''
class Solution:
    def getCount(self, head):
        # code here
        if head == None:
            
            return 0
            
        current = head
        
        count = 0
        
        while current:
            
            count += 1
            
            current = current.next
            
        return count
        