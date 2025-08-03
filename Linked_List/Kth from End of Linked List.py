
class Solution:
    def getKthFromLast(self, head, k):
        #code here
        
        if head ==None:
            
            return -1
            
        current = head
        
        list1 = []
        
        while current:
            
            list1.append(current.data)
            
            current = current.next
            
        
        
        if k <= len(list1):
            
            index = len(list1) - k
            
            return list1[index]
        else:
            return -1