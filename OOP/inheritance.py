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
#print(s.__brand)
print(s.price)
print(s.camera)
########## We cannot inherit the private member of a parent class########


############# Single level Inheritance
class Phone:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning phone")
    
class SmartPhone(Phone):
    pass

s = SmartPhone(1000,"Apple",12)
s.buy()


##### Multi-level Inheritance
class Product:
    def review(self):
        print("Product customer review")
        
class Phone(Product):

    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera
    
    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning phone")

class SmartPhone(Phone):
    pass

s = SmartPhone(10000, "1+", 12)
s.buy()
s.review()


###### Hierarchical inheritance
class Phone(Product):

    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera
    
    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning phone")

class SmartPhone(Phone):
    pass

class Feature_Phone(Phone):
    pass

s = SmartPhone(10000, "1+", 12)
s.buy()

f = Feature_Phone(10000, "1+", 12)
f.buy()


#### Multiple Inheritance
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print("Buying a phone")

class Product:
    
    def review(self):
        print("Customer review")

class SmartPhone(Phone, Product):
    pass

s = SmartPhone(20000, "Apple", 12)
s.buy()
s.review()


####### MRO- Methods resoultion Order example
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print("Phone buy method")

class Product:
    
    def buy(self):
        print("Product buy method")

class SmartPhone(Phone, Product):    ### Order matters here
    pass

s = SmartPhone(1000, "Apple", 12)
s.buy()

################ more example on inheritance
class A:
    
    def m1(self):
        return 20
    
class B(A):

    def m1(self):
        val = super().m1() + 30
        return val
    
class C(B):

    def m1(self):
        val = self.m1() + 20
        return val

c = C()
print(c.m1())