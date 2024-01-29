""" ---Create a class called Atm
    --- Create a constructor with two attributes
            pin and balance
    --- Create methods to create_pin, deposit, withdraw, check_balance and perform some 
    operations
"""

class Atm:

    def __init__(self):

        self.__balance = 0
        self.__pin = ""

        self.menu()

    def menu(self):
        user_input = input("""
                    Hello, how would you like to proceed?
                    1. Enter 1 to create pin
                    2. Enter 2 to deposit
                    3. Enter 3 to withdraw
                    4. Enter 4 to check balance
                    5. Enter 5 to exit
""")    
        if user_input == "1":
            #print("create pin")
            self.create_pin()
        elif user_input == "2":
            #print("Deposit")
            self.deposit()
        elif user_input == "3":
            #print("Withdraw")
            self.withdraw()
        elif user_input == "4":
            #print("Balance")
            self.check_balance()
        else:
            print("Bye")         



    def create_pin(self):
        self.__pin = input("Enter your pin ")
        print("Pin set successfully")

    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        if new_pin== str:
            self.__pin = new_pin
            print("Pin changed")
        else:
            print("not allowed")

    def deposit(self):
        temp = input("Enter your pin ")
        if temp == self.__pin:
            amount = int(input("Enter the amount to deposit "))
            self.__balance = self.__balance + amount
            print("Deposit successful")
        else:
            print("Invalid pin ")

    def withdraw(self):
        temp = input("Enter you pin ")
        if temp == self.__pin:
            amount = int(input("Enter your amount to withdraw "))
            if amount < self.__balance:
                self.__balance -= amount
                print("Withdrawn successful")
            else:
                print("Insufficient funds")
        else:
            print("Invalid pin")
    
    def check_balance(self):
        temp = input("Enter your pin ")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid pin")


sbi = Atm()
sbi.__pin = 'gftyu'   # __pin is private so we cannot changes it. __pin now refers to _Atm__pin
                      # we can change pin by using sbi._Atm__pin. but its best practice to
                    # create getter and setter methods to change it 
print(sbi.get_pin())
