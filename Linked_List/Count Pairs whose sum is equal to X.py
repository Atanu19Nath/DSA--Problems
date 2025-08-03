'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
'''
    head1:  head of linkedList 1
    head2:  head of linkedList 2
    n1:  len of  linkedList 1
    n2:  len of linkedList 1
    x:   given sum
'''
class Solution:
    def countPairs(self, head1, head2, x):
        # code here
        
        if head1 == None or head2 == None:
            
            return 0
            
        list1 = []
        
        list2 = []
        
        current = head1
        set1 = set()
        while current:
            
            if current.data not in set1:
                
                set1.add(current.data)
                list1.append(current.data)
            
            current = current.next
        
        current = head2
        count = 0
        while current:
            
            list2.append(current.data)
                
            if x - current.data in set1:
                count+=1
            
            current = current.next
            
        
        
        # set3 = set()
        
        # for i in list2:
            
        #     if i not in set3:
                
        #         set3.add(i)
                
        #         if x-i in set1:
                    
        #             count +=1
                    
                    
                    
        return count
        