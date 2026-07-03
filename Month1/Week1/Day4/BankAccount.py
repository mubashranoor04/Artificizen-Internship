#2. Create a BankAccount class with deposit() and withdraw() methods; prevent withdrawals beyond the balance.
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance= self.balance + amount

    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance= self.balance- amount
        else:
            print("Insufficient Balance")
account1 = BankAccount(18799)
account1.deposit(3500)
account1.withdraw(10500)
print(account1.balance)

account2 = BankAccount(18799)
account2.deposit(3500)
account2.withdraw(25000)
print(account2.balance)