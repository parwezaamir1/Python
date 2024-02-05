""" Aggreagate has-a relationship
eg. suppose there are two class
    1. customer
    2. Address

      So, here customer has-a relationship with address class
"""

class Customer:

    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.change_address(new_city, new_pin, new_state)

class Address:

    def __init__(self, city, pin, state):
        self.city = city
        self.pin = pin
        self.state = state

    def change_address(self, new_city, new_pin, new_state):
        self.city = new_city
        self.pin = new_pin
        self.state = new_state


add = Address("Kolkata", 123456, "WB")
cust = Customer("Zayd", "M", add)

cust.edit_profile("Zinnat", "Patna", 800002, "Bihar")
print(cust.address.pin)

print(cust.name)
print(cust.gender)
print(cust.address.pin)