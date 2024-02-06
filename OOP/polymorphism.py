############################# Polymorphism(multiple faces)
############ 1. Method Overriding
class Phone:

    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

class SmartPhone(Phone):

    def buy(self):                     #### method overriding
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
#print("Parent Num: ", c.get_num()) ####if child has constructor, then it can't invoke
                                  #Parent constructor



###############  2. Method Overloading
                     ###### Technically, method overloading doesnot exit in python, but we 
            # can achieve this by doing some modifiction in code\
##    Method overloading meanse same method having different input,  different behaviour

# class Geometry:

#     def area(self, a):
#         return 3.14 * a * a
    
#     def area(self, l, b):
#         return l * b
    
# g = Geometry()
# print(g.area(5))
                 ##### above code is true for Java but not for Python

class Geometry:

    def area(self, a, b=0):
        if b == 0:
            print("Circle: ", 3.14 * a * a )
        else:
            print("Rectangle: ", a * b)
    
g = Geometry()
g.area(4)
g.area(4, 5)
               #### we can achieve method overloading by using above code, just made b=0

