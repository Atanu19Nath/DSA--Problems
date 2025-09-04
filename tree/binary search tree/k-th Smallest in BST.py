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

def inorder_itr(root):

    stack = []
    result = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.data)
        current = current.right
    
    return result

def kthsmall(root,k):

    stack = []
    current = root

    count = 0

    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        count +=1

        if count == k:

            return current.data

        current = current.right
    
    return -1

values = [50, 30, 20, 40, 70, 60, 80] 

root = None

for value in values:

    root = insert(root,value)

print("preorder = ")
print(preorder(root))
print("inorder = ")
print(inorder_itr(root))
print("Kth Smallest = ",kthsmall(root,3))
