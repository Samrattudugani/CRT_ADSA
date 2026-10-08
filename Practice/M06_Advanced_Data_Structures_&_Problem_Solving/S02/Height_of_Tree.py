'''

binary tree should have atmost 2 nodes 

'''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def hei(self,root):
        if root is None:
            return -1
        else:
            lh = self.hei(root.left)
            rh = self.hei(root.right)
            if lh>rh:
                return lh+1
            else:
                return rh+1
    def isb(self,root):
        if root is None:
            return True
        else:
            lh = self.hei(root.left)
            rh = self.hei(root.right)
            if abs(lh - rh) <= 1:
                return self.isb(root.left) and self.isb(root.right)
            else:
                return False

    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("Height of tree is : ",root.hei(root))
# TREE IS BALANCED OR NOT
if root.isb(root):
    print("Tree is balanced Samrat")
else:
    print("Tree is not balanced Samrat")
if root.hei(root) != -1:
    print("Tree has a valid height")
else:
    print("Tree has an invalid height"  )

'''

################ every binary tree is a balanced tree but not every balanced tree is a binary tree #########################################

'''