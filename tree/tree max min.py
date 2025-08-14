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

def findmax(root):

    if root == None:

        return None
    
    current = root

    while current.right:
        
        current = current.right
         
    return current.data


def findmin(root):

    if root == None:

        return None
    
    current = root

    while current.left:
        
        current = current.left
         
    return current.data

def countnode(root):

    if root == None:
        
        return 0
    
    
    left = countnode(root.left)
    right = countnode(root.right)

    return 1 + left + right

def countedge(root):

    if root == None:
        return 0
    
    right = 0

    left = 0

    if root.right:

        right = 1+ countedge(root.right)

    if root.left:

        left = 1+ countedge(root.left)


    return left + right
    

    


   

root = None
values = [50, 30, 20, 40, 70, 60, 80]

for val in values:
    root = insert(root, val)

# print("Inorder traversal after insertion:")
# inorder(root)

# print("\nmax value = ",findmax(root))
# print("min value = ",findmin(root))


print(countnode(root))
print(countedge(root))