class Solution:
    def areIdentical(self, head1, head2):
        # Code here
        
        if head1 == None or head2 == None:
            return False
            
        current1 = head1
        current2 = head2
        
        while current1 and current2:
            
            if current1.data != current2.data:
                return False
                
            current1= current1.next
            current2= current2.next
        
        if current1 != None or current2 != None:
            return False
            
        return True
            