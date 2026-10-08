# LCA
# LOWEST COMMON ANCESTOR
from logging import root


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def lca(self,root,p,q):
        if root is None:
            return None
        if root == p or root == q:
            return root
    
        lh = self.lca(root.left,p,q)
        rh = self.lca(root.right,p,q)
        if lh is not None and rh is not None:
            return root
        if lh is not None:
            return lh 
        else:
            return rh
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right
print("LCA of the tree is : ", root.lca(root, root.left, root.right).data)