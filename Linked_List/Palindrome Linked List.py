
class Solution:
    def isPalindrome(self, head):
        #code here
        
        if head == None:
            
            return False
            
        list1 = []
        
        current = head
        
        while current:
            
            list1.append(current.data)
            
            current = current.next
        
      
        i = 0
        
        j = len(list1)-1
        
        while i < j:
            
            if list1[i] != list1[j]:
                return False
            
            i  +=1
            j  -=1
            
            
        return True