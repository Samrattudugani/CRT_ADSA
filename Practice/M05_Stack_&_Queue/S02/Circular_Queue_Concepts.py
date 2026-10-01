class Circular_Queue:
    def __init__(self,val):
        self . val = val


    def enq(self,val):
        if self.front == (self.rear + 1) % self.size:
            return "q is full"
        if self.front == -1:
            self.front = 0 
        self.rear = (self.rear+1)% self.size 
        self.q[self.rear] = val 
    def deq(self):

#prob: 20,232