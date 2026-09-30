class A:
    def s(self):
        print("A")

class B:
    def s(self):
        print("B")

def k(shape):
    shape.s()

k(A())
k(B())
