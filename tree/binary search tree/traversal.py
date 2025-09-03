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

def inorder(root):

    if root == None:

        return []
    
    return inorder(root.left) + [root.data] + inorder(root.right)

def postorder(root):

    if root == None:

        return []
    
    return postorder(root.left) + postorder(root.right) + [root.data]

def levelorder(root):


    queue = deque()

    if root == None:

        return []
    
    result = []
    
    queue.append(root)

    while queue:

        current = queue.popleft()

        result.append(current.data)

        if current.left:

            queue.append(current.left)
        
        if current.right:

            queue.append(current.right)

        
    return result





values = [50, 30, 20, 40, 70, 60, 80] 

root = None

for value in values:

    root = insert(root,value)

print("preorder = ")
print(preorder(root))
print("inorder = ")
print(inorder(root))
print("postorder = ")
print(postorder(root))
print("level order = ",levelorder(root))
