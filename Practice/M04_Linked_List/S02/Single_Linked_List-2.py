# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None 
# node1 = Node(10)
# node2 = Node(20)
# node1.next = node2
# node3 = Node(30)
# node2.next = node3
# def traverse():
#     current = node1
#     while current :
        
#         print(current.data, end=" -> ")
#         current = current.next
#     print("None")

def trverse(head):
    print("None")
"""
INSERTION 3 WAYS:
1. INSERTION AT THE BEGINING
2. INSERTION AT THE END
3. INSERTION AT A GIVEN POSITION

# 1. INSERTION AT THE BEGINING
CODE:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head

# Example Usage:
# Initial list: 10 -> 20 -> None
# insert_at_beginning(head, 5) -> 5 -> 10 -> 20 -> None

2. INSERTION AT THE END
CODE:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_end(head, data):
    new_node = Node(data)
    
    # If the list is empty, the new node becomes the head
    if head is None:
        return new_node
    
    # Traverse to the last node
    current = head
    while current.next is not None:
        current = current.next
        
    # Point the last node to the new node
    current.next = new_node
    return head

# Example Usage:
# Initial list: 10 -> 20 -> None
# head = insert_at_end(head, 30)
# Result list: 10 -> 20 -> 30 -> None 

3. INSERTION AT A GIVEN POSITION
CODE:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_position(head, data, position):
    # Position 0 means inserting at the beginning
    if position == 0:
        new_node = Node(data)
        new_node.next = head
        return new_node

    current = head
    count = 0

    # Traverse to the node just before the insertion index (position - 1)
    while current is not None and count < position - 1:
        current = current.next
        count += 1

    # If position is out of bounds (greater than list length)
    if current is None:
        print("Position out of bounds")
        return head

    # Create new node and adjust pointers
    new_node = Node(data)
    new_node.next = current.next
    current.next = new_node

    return headG

# Example Usage:
# Initial list: 10 -> 20 -> 30 -> None
# head = insert_at_position(head, 15, 1)  # Insert 15 at index 1
# Result list: 10 -> 15 -> 20 -> 30 -> None

DELETION 3 WAYS:
1.DELETION AT THE BEGINING
2.DELETION AT THE END
3.DELETION AT A GIVEN POSITION

#1. DELETION AT THE BEGINING
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_at_begining(head):
    if head is None:
        return None
    else:
        head = head.next
        return head

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

# 1. Create a linked list: 10 -> 20 -> 30 -> None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Original List:")
print_list(head)

# 2. Call the function and reassign the head variable
head = delete_at_begining(head)

print("\nAfter Deletion at Beginning:")
print_list(head)



def delebeg(head):
    if head is None:
        print("NONE")
        return
    newhead = head.next
    del head
    return newhead

#2. DELETION AT THE END
def deleend(head):
    if head is None:
        return None
    if head.next is None:
        del head
        return None
    current = head
    while current.next.next:
        current = current.next
    del current.next
    current.next = None
    return head 

#3. DELETION AT A GIVEN POSITION
def delepos(head, pos):
    if head is None:
        return None
    if pos == 0:
        newhead = head.next
        del head
        return newhead
    current = head
    for i in range(pos - 1):
        if current.next is None:
            return head  # Position is out of bounds
        current = current.next
    if current.next is None:
        return head  # Position is out of bounds
    temp = current.next
    current.next = temp.next
    del temp
    return head
"""
# Singly Linked List – Insertion and Deletion
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def insert_position(self, data, position):
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(position - 2):
            if temp is None:
                return
            temp = temp.next

        if temp is None:
            return

        new_node.next = temp.next
        temp.next = new_node

    def delete_beginning(self):
        if self.head is not None:
            self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    def delete_position(self, position):
        if self.head is None:
            return

        if position == 1:
            self.head = self.head.next
            return

        temp = self.head

        for i in range(position - 2):
            if temp.next is None:
                return
            temp = temp.next

        if temp.next is None:
            return

        temp.next = temp.next.next

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


ll = LinkedList()

ll.insert_beginning(20)
ll.insert_beginning(10)
ll.insert_end(40)
ll.insert_position(30, 3)

ll.display()

ll.delete_beginning()
ll.display()

ll.delete_end()
ll.display()

ll.delete_position(2)
ll.display()