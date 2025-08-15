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

def iterative_preorder(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)




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

print("\n preorder iterative")
print(iterative_preorder(root))



    
