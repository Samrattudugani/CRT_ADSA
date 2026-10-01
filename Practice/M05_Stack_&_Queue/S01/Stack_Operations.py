class StackWithTop:
    def __init__(self, size):
        self.capacity = size
        self.top = -1
        self.s = [None] * self.capacity

    def push(self, val):
        if self.top == self.capacity - 1:
            return "Stack is full"

        self.top += 1
        self.s[self.top] = val

    def is_empty(self):
        return self.top == -1

    def pop(self):
        if self.is_empty():
            return "Stack is empty"

        val = self.s[self.top]
        self.s[self.top] = None
        self.top -= 1
        return val

    def peek(self):
        if self.is_empty():
            return "Stack is empty"

        return self.s[self.top]

    def size(self):
        return self.top + 1


st = StackWithTop(5)

st.push(10)
st.push(20)
st.push(30)

print(st.is_empty())
print(st.peek())

st.pop()

print(st.peek())