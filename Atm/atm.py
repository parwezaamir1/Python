class Atm:

    def __init__(self):

        self.balance = 0
        self.pin = ""

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
        self.pin = input("Enter your pin ")
        print("Pin set successfully")

    def deposit(self):
        temp = input("Enter your pin ")
        if temp == self.pin:
            amount = int(input("Enter the amount "))
            self.balance = self.balance + amount
            print("Deposit successful")
        else:
            print("Invalid pin ")

    def withdraw(self):
        temp = input("Enter you pin ")
        if temp == self.pin:
            amount = int(input("Enter your amount "))
            if amount < self.balance:
                self.balance -= amount
                print("Withdrawn successful")
            else:
                print("Insufficient funds")
        else:
            print("Invalid pin")
    
    def check_balance(self):
        temp = input("Enter your pin ")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin")


sbi = Atm()
sbi.create_pin()
sbi.deposit()
sbi.check_balance()
sbi.withdraw()
sbi.check_balance()