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
        
        print("None")

# LENGTH OF LL
    def ll_lenght(self):

        if self.head == None:

            print('empty')

        else:
            current = self.head
            count = 0

            while current:

                count +=1
                current = current.next
            
        print(count)

    # return head

    def return_head(self):

        if self.head != None:
            return self.head
        else:
            return self.head
        
    #   SEARCH A ELEMENT
    def search(self,ele):

        if self.head == None:

            print("empty")
        else:

            current = self.head

            while current:

                if ele == current.data:

                    print("FOUND")
                    return
                current = current.next
            
            print("not found")




s= singlyll()


s.insert_begin(60)         # 1. Insertion at Beginning
s.insert_begin(50)
s.insert_begin(40)
s.insert_begin(30)
s.insert_begin(20)
s.insert_begin(10)           

s.display()                # 4. Display LL

#Lenght of linked list
s.ll_lenght()

#seach any element in LL
s.search(35)



