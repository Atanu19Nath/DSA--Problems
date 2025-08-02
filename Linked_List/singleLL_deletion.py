class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class singlyll:

    def __init__(self):
        self.head = None

    def insert_begin(self,data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def traversal (self):

        current = self.head

        while current != None:
            
            if current.next == None:
                return current
            current = current.next

        return current
    
    def insert_end(self,data):

        new_node = Node(data)

        end_node = self.traversal()

        end_node.next = new_node

    def insert_afterpos(self,data,pos):

        new_node = Node(data)
        
        count = 1

        current = self.head

        while current != None and count != pos:

            count +=1

            current = current.next
        
        print(current.data)
        new_node.next = current.next
        current.next = new_node

    def del_begin(self):

        if self.head != None:

            self.head = self.head.next
        else:
            print("empty")  

    def del_end(self):

        if self.head != None:
            current = self.head
            
            if current.next != None :
                
                current = current.next
                pre = self.head

                while current.next != None:

                    current = current.next
                    pre = pre.next

                pre.next = None    

            else:
                
                self.head = None
        else:
            print("empty")
    
    
    def display(self):

        if self.head != None:

            current = self.head

            while current != None:

                if current.next != None:
                    print(current.data,end="-->")
                else:
                    print(current.data,end="--->None")
                current = current.next
                
        else:
            print(self.head)
        
        print()


        
s = singlyll()

s.insert_begin(50)                 # 1. Insertion at Beginning
s.insert_begin(40)
s.insert_begin(30)
s.insert_begin(20)
s.insert_begin(10)

s.display() 

print("after deletion from end")
s.del_end()                          # 2. Delete from end
s.display() 

print("after deletion from begin")   # 3. Delete from begining
s.del_begin()
s.display()   