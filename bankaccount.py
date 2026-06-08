class BankAccount:
    def __init__(self, name, account_number, balance, date_opened):
        self.account_number = account_number
        self.balance = balance
        self.name = name
        self.date_opened = date_opened
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{amount} deposited successfully")

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(f"{amount} withdrawn successfully")

    def check_balance(self):
        print(f"This account has Ksh {self.balance}")

    def display_info(self):
        print("   Account Details    ")
        print(f"Account Name: {self.name}       Account Number: {self.account_number}        Balance : {self.balance}         Date opened : {self.date_opened}")


account_one = BankAccount("Hope", "Acc56473", 67000, "12-02-2019")
print(account_one.name)
print(account_one.account_number)
print(account_one.balance)
print(account_one.date_opened)
account_one.deposit(34500)
account_one.withdraw(7900)
account_one.check_balance()
account_one.display_info()

account_two = BankAccount("Nelly", "ACC8934", 456000, "23-10-2025")
print(account_two.name)
print(account_two.account_number)
print(account_two.balance)
print(account_two.date_opened)
account_two.deposit(4500)
account_two.withdraw(234)
account_two.check_balance()
account_two.display_info()