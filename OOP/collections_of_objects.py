class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        return "I am {} and my age is {}".format(self.name, self.age)

c1 = Customer('Zayd', 1)
c2 = Customer('Zinnat', 25)
c3 = Customer('Parwez', 29)

L = [c1, c2, c3]

for customer in L:
    print(customer.intro())
