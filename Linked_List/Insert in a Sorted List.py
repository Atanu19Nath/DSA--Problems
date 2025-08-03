class Solution:
    def sortedInsert(self, head, key):
        # code here
        # return head of edited linked list
        
        if head == None:
            
            return head
            
        
        
        if key < head.data:
            
            new_node = Node(key)
            
            new_node.next = head
            
            head = new_node
            
            return head
            
        pre = head    
        current = head.next
        
        while current:
            
            if key > pre.data and key <= current.data:
                
                new_node = Node(key)
                
                pre.next = new_node
                
                new_node.next = current
                
                return head
                
            pre = pre.next
            current = current.next
            
        if current == None and pre:
            
            if key > pre.data:
                
                 new_node = Node(key)
                 
                 pre.next = new_node
                
  
                
            
        return head