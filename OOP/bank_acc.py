class BankAccount:
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


acct = BankAccount("Darcy")
print(acct.owner)  # Darcy
print(acct.getBalance())  # 0.0
print(acct.deposit(10))  # 10.0
print(acct.withdraw(3))  # 7.0
print(acct.getBalance())  # 7.0
