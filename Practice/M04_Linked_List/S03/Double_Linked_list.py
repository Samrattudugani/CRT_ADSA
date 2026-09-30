
"""
# """
# DOUBLE LINKED LIST :
# NODE HAS 3 PARTS :
# 1.DATA
# 2.PREV
# 3.NEXT
# """
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)

# node1.next = node2
# node2.prev = node1
# node2.next = node3
# node3.prev = node2
# node3.next = node4
# node4.prev = node3

# def traverse_forward(head):
#     temp = head
#     while temp:
#         print(temp.data, end=" <<----->> ")
#         temp = temp.next
#     print("None")

# traverse_forward(node1)

# def reverse_traverse(tail):
#     temp = tail
#     while temp:
#         print(temp.data, end=" <<----->> ")
#         temp = temp.prev
#     print("None")

# reverse_traverse(node4) 

# def insert_beginning(head, data):
#     new_node = Node(data)
#     new_node.next = head
#     if head is not None:
#         head.prev = new_node
#     head = new_node
#     return head 
# # def traverse_forward(head):
# #     temp = head
# #     while temp:
# #         print(temp.data, end=" <<----->> ")
# #         temp = temp.next
# #     print("None")
# head = None
# head = insert_beginning(head, 10)
# head = insert_beginning(head, 20)
# head = insert_beginning(head, 30)
# print("After inserting at the beginning:")
# traverse_forward(head)
# print() 


# def ins_end(tail,data):
#     newnod = Node(data)
#     tail.next = newnod
#     newnod.prev = tail
#     return newnod


'''
Double Linked List :
Data store Nodes
1. data
2. prev
3. next

Algorithm :
1. Create Nodes
2. Insert data
3. Connection between nodes
4. Traverse
'''
'''
# FORWARD 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
def traverse():
    curr = node1
    while curr:
        print(curr.data, end="<->")
        curr = curr.next
    print("None")
traverse()

# REVERSE 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
def traverse_reverse():
    curr = node4
    while curr:
        print(curr.data, end="<->")
        curr = curr.prev
    print("None")
traverse_reverse()
'''
'''
# Insertion at the beginning:
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
def insert_begin(head, data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node
def traverse_ins(head):
    curr = head
    while curr :
        print(curr.data, end="<->")
        curr = curr.next
    print("None")
head = None
head = insert_begin(head, 10)
head = insert_begin(head, 30)
head = insert_begin(head, 50)
head = insert_begin(head, 530)
print("Insertion at the beginning")
traverse_ins(head)
print()  

# Insertion at the end:

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def insert_end(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    temp = head
    while temp.next:
        temp = temp.next

    temp.next = new_node
    new_node.prev = temp

    return head

def traverse(head):
    temp = head
    while temp:
        print(temp.data, end="<->")
        temp = temp.next
    print("None")
head = None

head = insert_end(head, 10)
head = insert_end(head, 30)
head = insert_end(head, 50)
head = insert_end(head, 200)
head = insert_end(head, 3456)
print("Insertion at the end")
traverse(head) 


# Insertion at the Position:
def insert_at_position(head, data, position):
    new_node = Node(data)
    new_node.prev = Node

    if position == 1:
        new_node.next = head
        if head:
            head.prev = new_node
        return new_node

    temp = head

    for i in range(position - 2):
        if temp is None:
            return head
        temp = temp.next

    if temp is None:
        return head

    new_node.next = temp.next
    new_node.prev = temp

    if temp.next:
        temp.next.prev = new_node

    temp.next = new_node

    return head

'''

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    class DLL:
        def __init__(self):
            self.head = None
        def inb(self,data):
            new = Node(data)
            new.next = self.head
            if self.head:
                self.head.prev = new
            return new 
        def trav(self):
            curr = self.head
            while curr:
                print(curr.data, end = "<---->")
                curr = curr.next 
            print("None")
dl = DLL()
dl.head = dl.inb(10)
dl.head = dl.inb(20)
dl.head = dl.inb(30)