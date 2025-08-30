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

# recursive approach [ O(n)]
def btreemax(root):

    if root == None:

        return float("-inf")

    right_subtree = btreemax(root.right)

    return max(root.data,right_subtree)

#iterative approach

def btreemax2(root):

    if root == None:

        return None
    
    current = root

    while current.right:

        current = current.right

    return current.data




values = [50, 30, 20, 40, 70, 60, 80] 

root = None

for value in values:

    root = insert(root,value)

print("preorder = ")
print(preorder(root))

print("Tree Max =", btreemax2(root))