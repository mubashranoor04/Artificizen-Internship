#2. Define a custom exception InsufficientBalanceError and raise it inside the BankAccount class from Day 4.
class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            raise InsufficientBalanceError("Insufficient Balance")
        
account1 = BankAccount(18799)
account1.deposit(3500)
try:
    account1.withdraw(10500)
    print(account1.balance)
except InsufficientBalanceError as error:
    print(error)

account2 = BankAccount(18799)
account2.deposit(3500)
try:
    account2.withdraw(25000)
    print(account2.balance)
except InsufficientBalanceError as error:
    print(error)