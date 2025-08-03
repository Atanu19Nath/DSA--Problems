'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        
        
        if head == None:
            
            return head
            
        current = head
        
        set1 = set()
        
        result = []
        
        while current:
            
            if current.data not in set1:
                
                result.append(current.data)
                set1.add(current.data)
            
            current = current.next
            
            
        head2 = None
        
        # print(result)
        
        for i in range(len(result)-1,-1,-1):
            
            new_node = Node(result[i])
            
            if head2 == None:
                
                head2 = new_node
            else:    
                
                new_node.next = head2
            
                head2 = new_node
            
        head = head2
        
        return head
            
                
        