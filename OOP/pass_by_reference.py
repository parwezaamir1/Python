class Customer:

    def __init__(self, name):
        self.name = name

def greet(customer):
    # if customer.gender == 'Male':
    #     print("Hello", customer.name, 'sir')
    # else:
    #     print("Hello", customer.name, "ma'am")
    print(id(customer))

cust = Customer("Nitish")  # here cust acts as a reference variable of Object Customer
print(id(cust))

greet(cust)

b = 3      #here a and b pointing to same memory location, called pass-by-reference variable
print(id(b))  # if a changes b changes, if b changes a also changes
a = b
print(id(a))
