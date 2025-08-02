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


    def display(self):

        if self.head != None:

            current = self.head

            while current != None:

                print(current.data,end="-->")
                
                current = current.next
        else:
            print(self.head)

s = singlyll()

s.insert_begin(100)         # 1. Insertion at Beginning
s.insert_begin(80)
s.insert_begin(70)
s.insert_begin(50)
s.insert_begin(40)
s.insert_end(10)           # 2. Insertion at End
s.insert_end(20)

s.insert_afterpos(76,3)    # 3. Insertion at any position


s.display()                # 4. Display LL