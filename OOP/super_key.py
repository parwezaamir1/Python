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
        super().buy()            ### to invoke the parent methods
         ### We can use super keyword only inside class not outside of class
         # Using super, we can only invoke Parents Constructor,methods but not attributes

s = SmartPhone(10000, "Apple", 12)
s.buy()
#s.super().buy()            ### we can not use super like this, use only inside the class



####### Super with constructor
class Phone:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("Inside smartphone constructor")

s = SmartPhone(10000, "1+", 12, "android", 8)

print(s.os)
print(s.brand)


###### More Example on super
class Parent:

    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num
    
class Child(Parent):

    def __init__(self, num, val):
        super().__init__(num)
        self.__val = val

    def get_val(self):
        return self.__val
    
c = Child(100, 200)
print(c.get_num())
print(c.get_val())

    
############## example on super
class Parent:

    def __init__(self):
        self.num = 100

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.val = 200

    def show(self):
        print(self.num)    ##### we can use the parent attribute when we call from child
        print(self.val)

c = Child()
c.show()

#### more example 
class Parent:
    def __init__(self):
        self.__num = 100
    
    def show(self):
        print("Parent:", self.__num)

class Child(Parent):

    def __init__(self):
        super().__init__()
        self.__val = 200

    def show(self):
        print("Child: ", self.__val)

p = Parent()
p.show()
c = Child()
c.show()
