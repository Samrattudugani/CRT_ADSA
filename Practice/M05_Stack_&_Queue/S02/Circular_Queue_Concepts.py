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
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in mapping: 
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:  
                stack.append(char)
        
        return not stack

#232
class MyQueue:

    def __init__(self):
      self.ins=[]
      self.os = []
        

    def push(self, x: int) -> None:
        self.ins.append(x)

    def pop(self) -> int:
        self.peek()
        return self.os.pop()

    def peek(self) -> int:
        if not self.os:
          while self.ins:
            self.os.append(self.ins.pop())
        return self.os[-1]

    def empty(self) -> bool:
      return not self.ins and not self.os