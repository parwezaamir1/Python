# Inheriting the constructor
class Phone:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    pass

s = SmartPhone(10000, "1+", 12)
print(s.brand)
print(s.price)
print(s.camera)
########## We can inherit the constructor of a parent class########


###### Inheriting Private members
class Phone:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera

class SmartPhone(Phone):
    pass

s = SmartPhone(10000, "1+", 12)
print(s.__brand)
print(s.price)
print(s.camera)
########## We cannot inherit the private member of a parent class########






