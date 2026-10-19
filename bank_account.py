
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Please enter a valid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully.")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance: ", self.balance)


account = BankAccount("Shiva", 5000)

account.display_balance()
account.deposit(1000)
account.withdraw(500)
account.display_balance()
