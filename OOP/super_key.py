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
         # Using super, we can only invoke Parents Constructor and methods not attributes

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
