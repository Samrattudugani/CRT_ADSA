'''

class Queue:
    def __init__(self,size):
        self.size = size 
        self.front = -1
        self.rear = -1 
        self.q = [None] * self.size
        def enq(self,val):
            self.val = val 
            if self.rear == self.size -1:
                return "q is full"
            self.rear += 1
            self.q[self.rear] = val 
        def deq(self):
            if self.front == -1:
                return "q is empty"
            del.self.empty
            self.front += 1



# DEQUEUE and ENQUEUE

class Queue:
    def __init__(self, size):
        self.size = size
        self.q = [None] * size
        self.front = self.rear = -1

    def enq(self, item):
        if self.rear == self.size - 1:
            return 
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.q[self.rear] = item

    def deq(self):
        if self.front == -1:
            return None
        val = self.q[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front += 1
        return val 

    def dis(self):
        if self.front != -1:
            for i in range(self.front, self.rear + 1):
                print(self.q[i], end=" ")
            print()
q = Queue(3)
q.enq(10)
q.enq(20)
q.enq(30)
q.dis()
q.deq()
q.dis()
q.enq(40)
q.dis()

'''
# Queue USING LinkED LIsT
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None # Initialize next as None

class qll:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enq(self, item):
        new_node = Node(item)
     
        if self.front is None:
            self.front = self.rear = new_node
            return
      
        self.rear.next = new_node
        self.rear = new_node

    def deq(self):
      
        if self.front is None:
            return None
    
        val = self.front.data
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        return val 

    def dis(self):
        if self.front is None:
            print("Queue Empty")
            return
        temp = self.front
        while temp:
            print(temp.data, end="--> ")
            temp = temp.next
        print()

q = qll() 
q.enq(10)
q.enq(20)
q.enq(30)
q.dis()

q.deq()
q.dis()

q.enq(40)
q.dis()