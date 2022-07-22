class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amount):
        self.balance += dep_amount
        return f"Amount {dep_amount} deposited!"

    def withdraw(self, withdraw_amt):
        if self.balance >= withdraw_amt:
            return f"withdraw amount {withdraw_amt} successfully"
        else:
            return f"no longer can withdraw as available balance is {self.balance}"

    def __str__(self):
        return f'Owner: {self.owner} \nBalance: {self.balance}'


account = Account("Jose", 100)
print(account)
print(account.owner)
print(account.balance)
print(account.deposit(50))
print(account.withdraw(75))
print(account.withdraw(500))
