from collections import deque

class Node:

    def __init__(self,data):

        self.data = data
        self.left = None
        self.right = None

def insert(root,value):

    if root == None:

        new_node = Node(value)  
        return new_node
        
    elif value < root.data:

        root.left = insert(root.left,value)

    elif value > root.data:

        root.right = insert(root.right,value)

    return root

def preorder(root):

    if root == None:

        return []

    return [root.data] + preorder(root.left) + preorder(root.right)

def rrl(root):

    if root == None:

        return []
    
    return  rrl(root.right) + [root.data] + rrl(root.left)

def kthlargest(root,k):

    if root == None:

        return -1
    
    stack = []
    count = 0

    current = root

    while stack or current:

        while current:

            stack.append(current)
            current = current.right

        temp = stack.pop()

        count +=1

        if count == k:
            
            return temp.data
        
        current = temp.left

    return -1


values = [50, 30, 20, 40, 70, 60, 80] 

root = None

for value in values:

    root = insert(root,value)

print("preorder = ")
print(preorder(root))

print("right,root,left= ", rrl(root))

print("kthlargest = ",kthlargest(root,3))
