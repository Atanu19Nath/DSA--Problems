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

def show_range_node(root,l,r):

    if root == None:

        return 0
    
    current = root

    stack = []

    result = []

    while stack or current:

        while current:

            stack.append(current)

            if current.data > l:
                current = current.left
            else:
                break

        temp = stack.pop()
        
        if temp.data >= l and temp.data <= r:

            result.append(temp.data)


        if temp.data < r:

            current = temp.right

        else:

            current = None

    
    return result


def range_sum2(root,l,r):

    if root == None:

        return []
    
    left_subtreesum = range_sum2(root.left,l,r)

    right_subtreesum = range_sum2(root.right,l,r)


    if root.data >=l and root.data <=r:

        return [root.data] + left_subtreesum + right_subtreesum
    else:
        return left_subtreesum + right_subtreesum
    
def path(root,key):

    if root == None:

        return -1
    
    path = []

    current = root

    result = []

    while current:

        path.append(current.data)

        if key < current.data:

            current = current.left

        elif key > current.data:

            current = current.right

        elif key == current.data:

            return path

                
    return -1
            
    




values = [50, 30, 20, 40, 70, 60, 80] 

root = None

for value in values:

    root = insert(root,value)

print("preorder = ")
print(preorder(root))


print(" path from root = ", path(root,45))