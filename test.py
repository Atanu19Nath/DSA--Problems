class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class singlyll:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_begin(self,data):

        new_node = Node(data)

        if self.head == None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    
    def display(self):

        current = self.head

        while current != None:

            print(current.data)

            current = current,next


s = singlyll()

s.insert_begin(10)

s.display
