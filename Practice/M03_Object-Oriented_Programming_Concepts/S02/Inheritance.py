'''
Inertance in Python
Inheritance is a way of creating a new class from an existing class. The new class is called
the derived class or child class, and the existing class is called the base class or parent class. 
The derived class inherits the attributes and methods of the base class, allowing for code reuse and 
the creation of a hierarchical relationship between classes.
Types:

1. Single Inheritance: A derived class inherits from a single base class.
2. Multiple Inheritance: A derived class inherits from multiple base classes.
3. Multilevel Inheritance: A derived class inherits from a base class, which in turn inherits from another base class.
4. Hierarchical Inheritance: Multiple derived classes inherit from a single base class.
5. Hybrid Inheritance: A combination of two or more types of inheritance.

Key words in inheritance:

Singel inheritance

class a:
    def display(self):
        print("THIS IS A")
class b(a):
    def display2(self):
        print("THIS IS B")
b = b()
b.display()
b.display2()


MULTILEVEL

class a:
    def display1(self):
        print("this is a")
class b(a):
    def display2(self):
        print("THIS IS B")
class c(b):
    def display3(self):
        print("THIS IS C ")
c = c()
c.display1()
c.display2()
c.display3()

Multiple 

class A:
    def d1(self):
        print("THIS IS A")

class B:
    def d2(self):
        print("THIS IS B")

class C(A, B):
    def d3(self):
        print("THIS IS C")

obj = C()

obj.d1()
obj.d2()
obj.d3()



Hierarical 
class a:
    def d1(self):
        print("THIS IS A")
class b(a) :
    def d2(self):
        print("THIS IS B") 
class c(a):
    def d3(self):
        print("THIS IS C")
b = b()
c = c()

b.d1()
b.d2()

c.d1()
c.d3()
'''