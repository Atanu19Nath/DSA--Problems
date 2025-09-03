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

def inorder_presuc(root,key):

    if root == None:

        return Node(-1),Node(-1)
    
    current = root

    pre = None

    suc = None

    while current:
    
        if current.data < key :

            pre = current
            current = current.right

        elif current.data > key:

            suc = current

            current = current.left

        else:

            if current.left:

                temp = current.left

                while temp.right:

                    temp = temp.right

                pre = temp
            
            if current.right:

                temp = current.right

                while temp.left:

                    temp = temp.left

                suc = temp

            break  

    return pre,suc
    

values = [50, 30, 20, 40, 70, 60, 80] 


root = None

for value in values:

    root = insert(root,value)

print("preorder = ")
print(preorder(root))


pre , suc = inorder_presuc(root,65)

print("predesessor : ",pre.data)
print("Successor : ",suc.data)
