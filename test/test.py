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


def paths(root):

    if root == None:

        return []
    
    stack = []

    queue = []

    result = []

    current = root

    while stack or current:

        while current:

            stack.append(current)

            queue.append(current.data)

            current = current.left

        temp = stack.pop()

        if temp.left == None and temp.right == None:

            ans = queue.copy()

            result.append(ans)

            queue.pop()

    
        current = temp.right


    return result






values = [50, 30, 20, 40, 70, 60, 80] 

root = None

for value in values:

    root = insert(root,value)

print("preorder = ")
print(preorder(root))

print("All path from root to leaf = ",paths(root))