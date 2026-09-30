'''
poly - many 
morph - forms 
types of polymorphism:
1 compile time polymorphism (static polymorphism)

2 run time polymorphism (dynamic polymorphism)

def add(a,b):
    return a + b 
def add(a,b,c):
    return a+b+c 
def add(a,b,c,d):
    return a+b+c+d 
print(add(1,2))
print(add(1,2,3))
print(add(1,2,3,4))

Python does not support Function overloading directly.
we can achieve function overloading by using default


def add(*values):
    return sum(values)
print(add(10,20))
print(add(10,20,30))

Operator overloading

class A:
    def __init__(self,x):
        self.x = x 
    def __add__(self,val):
        return self.x + val.x
    def __sub__(self,val):
        return self.x - val.x
    def __lt__(self,val):
        return self.x < val.x
a = A(10)
b = A(20)
print(a+b)
print(a-b)
print(a < b)


class B:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    def __add__(self,val):
        return self.x + val.x,self.y+val.y 
    def __sub__(self,val):
        return self.x - val.x , self.y-val.y 
a = B(1,2)
b = B(3,4)
print(a+b)
print(a-b) 
'''
Method overriding :
def add(a,b):
    return a + b
def add(a,b,c):
    return a+b+c   
