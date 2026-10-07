class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# TREE STRUCTURE
root = Node(1)
root.right = Node(2)
root.left = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


# =========================
# DFS TRAVERSALS
# =========================

# 1. PREORDER
# ROOT - LEFT - RIGHT
def preorder(root):
    if root:
        print(root.data, end=" -> ")
        preorder(root.left)
        preorder(root.right)


# 2. INORDER
# LEFT - ROOT - RIGHT
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" -> ")
        inorder(root.right)


# 3. POSTORDER
# LEFT - RIGHT - ROOT
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end="  -> ")


# =========================
# BFS TRAVERSAL
# =========================

# LEVEL ORDER
def bfs(root):
    if root is None:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)

        print(node.data, end=" -> ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


# =========================
# OUTPUT
# =========================

print("PREORDER TRAVERSAL:")
preorder(root)

print("\nINORDER TRAVERSAL:")
inorder(root)

print("\nPOSTORDER TRAVERSAL:")
postorder(root)

print("\nBFS TRAVERSAL:")
bfs(root)