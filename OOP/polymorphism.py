############ Method Overriding
class Phone:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

class SmartPhone(Phone):

    def buy(self):
        print("Buying a smartphone")

s = SmartPhone(10000, "Apple", 12)
s.buy()



##### Example 1
class Parent:

    def __init__(self, num):
        self.__num = num
    
    def get_num(self):
        return self.__num
    
class Child(Parent):

    def show(self):
        print("This is in child class")

c = Child(1000)
print(c.get_num())
c.show()


####### Example 2
class Parent:

    def __init__(self,num):
        self.__num = num
    
    def get_num(self):
        return self.__num
    
class Child(Parent):

    def __init__(self, val, num):
        self.__val = val
    
    def get_val(self):
        return self.__val
    
c = Child(100, 10)
print("Parent Num: ", c.get_num()) ####if child has constructor, then we cann't call Parent constructor

