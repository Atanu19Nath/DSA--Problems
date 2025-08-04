
class Solution:
    def constructLL(self, arr):
        # code here
        
        head = None
        tail = None
        
        for i in arr:
            new_node = Node(i)
            if head == None:
                head = new_node
                tail = new_node
                
            else:
                
                tail.next = new_node
                
                tail = new_node
                
        
        return head