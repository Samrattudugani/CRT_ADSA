# '''

# 🌳 Binary Search Tree (BST) in Python

# 1. What is a BST?

# A Binary Search Tree is a binary tree that follows three rules:

# Left subtree: Contains values smaller than the root.
# Right subtree: Contains values greater than the root.
# Each node can have at most two children.
# Example

# Consider this BST:

# #         50
# #        /  \
# #       30   70
# #      / \   / \
# #     20 40 60 80
# # Root = 50
# Left child of 50 = 30
# Right child of 50 = 70
# 20 is smaller than 50 and 30.
# 80 is greater than 50 and 70.

# Remember: Left < Root < Right.

# OPERATIONS:
# 1.SEARCH
# 2.INSERT
# 3.DELETE
# 4.VALIDATION 
# 5.TRAVERSE

# ALGO:
# 1.CHECK WITH ROOT NODE
# 2.IF K == ROOT RETURN TRUE
# 3.IF K > ROOT SEARCH IN RIGHT SUB TREE
# 4. IF K < ROOT SEARCH IN LEFT SUB TREE


# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.left = None
# #         self.right = None
# #     def bst(root,k):
# #         if root is None:
# #             return False
# #         if root.data == k:
# #             return True
# #         if k > root.data :
# #             return bst(root.right,k)
# #         else:
# #             return bst(root.left,k)
        


# # root = Node(50)
# # root.left = Node(30)
# # root.right = Node(70)
# # root.left.left = Node(20)
# # root.left.right = Node(40)
# # root.right.left = Node(60)
# # root.right.right = Node(80)
# # print(bst(root,60))
# # print(bst(root,90))
#'''
## 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bst(root, k):
    if root is None:
        return False
    if root.data == k:
        return True
    if k > root.data:
        return bst(root.right, k)
    else:
        return bst(root.left, k)

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)
root.right.right.right = Node(1000)

print(bst(root, 60))
print(bst(root, 90))
print(bst(root,70))
print(bst(root,1000))