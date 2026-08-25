'''
#  binding data and methods together in a single unit is called encapsulation it also hide data 
# we hide data using acsess specifiers like private, protected and public:
# data hiding means that the internal object details are hidden from the outside world and only the necessary information is provided to the outside world.

Data hiding using access specifiers:

Public : 
    - Public members are accessible from anywhere in the program.
    - They can be accessed by any other class or function.
    - In Python, all members are public by default.

    Protected : (_)
    - Protected members are accessible within the class and its subclasses.
    - They are indicated by a single underscore prefix (_).

    Private : (__)
    - Private members are accessible only within the class. 

class a:
    a = 10
    _b= 20
    __c = 30
obj = a()
print(obj.a) # 10
print(obj._b) # 20
print(obj._a__c) # 30


Access and modify private members using getter and setter methods:
'''
class bank:
    def __init__(self, bal):
        self.__bal = bal
    def credit(self,amt):
        self.__bal += amt 
    def debit(self,amt):
        self.__bal -= amt 
    def get_bal(self):
        return self.__bal
b = bank(100000000)
print(b.get_bal())
b.credit(50000)
print(b.get_bal())
b.debit(200000)
print(b.get_bal())

