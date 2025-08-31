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

def isBST(root):

    
    def helper(root,lower_range,higher_range):
            
            if root == None:

                return True
            
            if root.data <= lower_range or root.data >= higher_range:

                return False

                
            left_subtree = helper(root.left,lower_range,root.data)

            right_subtree = helper(root.right,root.data,higher_range)  


            return left_subtree and right_subtree   
    
    lower_range  = float('-inf')
    higher_range = float('inf')
    
    return helper(root,lower_range,higher_range)
    



values = [50, 30, 20, 40, 70, 60, 80] 


root = None

for value in values:

    root = insert(root,value)

print("preorder = ")
print(preorder(root))

print("check is it BST = ",isBST(root))
