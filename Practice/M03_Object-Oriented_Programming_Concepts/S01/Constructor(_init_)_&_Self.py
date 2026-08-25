# from math import pi
# from turtle import circle
# class circle:
#     r = 9 
#     co = 0
#     def __init__(self):
#         circle.co += 1
#     def area(self):
#         print(pi*(self.r*self.r))
#     def peri(self):
#         print(2*pi*self.r)  
# c1 = circle()
# c2 = circle()
# c1.area()
# c2.peri()
# print(circle.co)
# from math import pi
# from turtle import circle
# class circle:
#     def __init__(self, r):
#         self.r = r
 
#     def area(self):
#         return pi*(self.r*self.r)
#     def peri(self):
#         return 2*pi*self.r  
# c1 = circle(4)
# c2 = circle(6100)
# print(c1.area())
# print(c2.peri())
# print(c1.peri())
# print(c2.area())


# #1603
# class ParkingSystem:

#     def __init__(self, big: int, medium: int, small: int):
#       self.big = big
#       self.medium = medium
#       self.small = small 
        

#     def addCar(self, carType: int) -> bool:
#       if carType == 1:
#         if self.big > 0:
#           self.big -= 1
#           return True
#       if carType == 2:
#         if self.medium > 0:
#           self.medium -= 1
#           return True 
#       if carType == 3:
#         if self.small > 0:
#           self.small -= 1
#           return True 
#       return False

# class ParkingSystem:

#     def __init__(self, big: int, medium: int, small: int):
#       self.slots = [0,big,medium,small]
#     def addCar(self, carType: int) -> bool:
#       if self.slots[carType] > 0:
#         self.slots[carType] -= 1
#         return True 
#       return False
        
#1845