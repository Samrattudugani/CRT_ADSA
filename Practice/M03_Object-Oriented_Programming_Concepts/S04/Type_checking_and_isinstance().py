# # Type checking is a process of verifying the type of a variable or object in programming. In Python, you can use the `isinstance()` function to check if an object is an instance of a specific class or a subclass thereof.
# a = 10
# b = "Hello"
# c = [1, 2, 3]
# d = {"name": "John", "age": 30}
# e = (1, 2, 3)
# f = 3.14 
# g = {1, 2, 3}
# h = None
# i = True
# print(type(a))  # <class 'int'>
# print(type(b))  # <class 'str'>
# print(type(c))  # <class 'list'>
# print(type(d))  # <class 'dict'>
# print(type(e))  # <class 'tuple'>
# print(type(f))  # <class 'float'>
# print(type(g))  # <class 'set'>
# print(type(h))  # <class 'NoneType'>
# print(type(i))  # <class 'bool'> 
# print("")
# #isinstance() function is used to check if an object is an instance of a specific class or a subclass thereof. It returns True if the object is an instance of the specified class or a subclass, and False otherwise.
# print(isinstance(a, int))  # True
# print(isinstance(b, str))  # True
# print(isinstance(c, dict))  # False
# print(isinstance(c, list))  # True
# print(isinstance(d, dict))  # True
# print(isinstance(e, tuple))  # True
# print(isinstance(f, int))  # False
# print(isinstance(f, float))  # True
# print(isinstance(g, set))  # True
# print(isinstance(h, type(None)))  # True
# print(isinstance(i, bool))  # True

# a = 34567
# if isinstance(a, str):
#     print("a is a string")
# else:
#     print("a is a number") 
#


# #CHECKING OF OBJECTS CLASS :
# class a:
#     def display(self):
#         print("THIS IS A")
# class b(a):
#     def display(self):
#         print("THIS IS B")
# b = b()
# print(isinstance(b, a))  # True

# print(isinstance(b, object))  # True
# print(isinstance(b, str))  # False

# def process(d):
#     if isinstance(d, int):
#         return d * 2
#     elif isinstance(d, str):
#         return d.upper()
#     elif isinstance(d, list):
#         return len(d)
#     else:
#         return "Unsupported type" 
# print(process(100))  # Output: 200
# print(process("hello"))  # Output: HELLO
# print(process([1, 2, 3, 4]))  # Output: 4
# print(process({"name": "John"}))  # Output: Unsupported type

##INTERVIEW PURPOSE:
# class a:
#     def display(self):
#         print("THIS IS A")
# class b(a):
#     def display(self):
#         print("THIS IS B")
# obj = b()
# print(isinstance(obj, a))  # True
# print(isinstance(obj, b))  # True
# print((type(obj) == b))  # True
# print((type(obj) == a))  # False 
# print(isinstance(obj, object))  # True
# print(isinstance(obj, str))  # False
