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




def delete_node(root,value):

    if root == None : 

        return root
    
    if value < root.data:

        root.left = delete_node(root.left,value)

    elif value > root.data:

        root.right = delete_node(root.right,value)

    else:

        # No left child

        if root.left == None :

            return root.right
        
        # No right child

        if root.right == None:

            return root.left
        
        # Havng both child

        if root.left and root.right:

            current = root.left

            while current.right:

                current = current.right

            current.right = root.right

            return root.left
        

    return root







values = [50, 30, 20, 40, 70, 60, 80] 

root = None

for value in values:

    root = insert(root,value)

print("preorder = ")
print(preorder(root))

root = delete_node(root,50)


print("preorder after delete= ")
print(preorder(root))