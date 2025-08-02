class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):

        return self.arr.append(data)

    #Function to remove an item from top of the stack.
    def pop(self):

        if self.arr: 
            return self.arr.pop()
        return -1

    def display(self):

        for i in self.arr:
            
            print(i,end="<----")
        
stack = MyStack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.display()



        