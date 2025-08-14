class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,val):

    if root == None:

        root = Node(val)
        return root
    
    elif val < root.data:

        root.left = insert(root.left,val)

    elif val > root.data:

        root.right = insert(root.right,val)
    
    return root

def inorder(root):

    if root == None:
        return 
    
    inorder(root.left)
     
    print(root.data, end=" ")

    inorder(root.right)

def preorder(root):

    if root == None:
        return
    
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)
    
def postorder(root):

    if root == None:
        return
    postorder(root.left)
    postorder(root.right)

    print(root.data, end=" ")

def levelorder(root):

    if root == None:
        return 
    
    print(root.data,end=" ")

    if root.left:
        print(root.left.data)
    if root.right:
        print(root.right.data)
    
    levelorder(root.left)
    levelorder(root.right)





root = None
values = [50, 30, 20, 40, 70, 60, 80]

for val in values:
    root = insert(root, val)

print("Inorder traversal after insertion:")
inorder(root)
print("\npreorder traversal after insertion:")
preorder(root)
print("\npostorder traversal after insertion:")
postorder(root)

print("\nlevelorder traversal after insertion:")
print(levelorder(root))



    
