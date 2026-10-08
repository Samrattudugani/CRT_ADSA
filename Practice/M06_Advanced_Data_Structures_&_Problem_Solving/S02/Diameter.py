'''
LONGEST PATH B/W NODES IN A TREE
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return -1
    return max(height(root.left), height(root.right)) + 1

def diameter(root):
    if root is None:
        return -1

    d = height(root.left) + height(root.right) + 2

    return max(d, diameter(root.left), diameter(root.right))
def lca(root,n1,n2):
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Diameter of the tree is : ", diameter(root))


# LCA
# LOWEST COMMON ANCESTOR
