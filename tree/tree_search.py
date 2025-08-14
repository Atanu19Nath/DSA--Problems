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


def search(val,root):

    if root == None :
        return False

    if root.data == val:

        return True
    
    if val < root.data:
        
        return search(val,root.left)
    
    if val > root.data:

        return search(root.right)


root = None
values = [50, 30, 20, 40, 70, 60, 80]

for val in values:
    root = insert(root, val)

print("Inorder traversal after insertion:")
inorder(root)

print(search(40,root))


    
