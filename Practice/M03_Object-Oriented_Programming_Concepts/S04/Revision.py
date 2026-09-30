# TYPES OF INHERITANCE
# 1. Single Inheritance: A derived class inherits from a single base class.
# code : 
def si():
    class A:
        def display1(self):
            print("this is a")
    class B(A):
        def display2(self):
            print("THIS IS B")
    b = B()
    b.display1()
    b.display2()