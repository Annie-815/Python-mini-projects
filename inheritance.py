class bank_account:
    def __init__(self, account_name, account_no, balance=0):
        self.account_name = account_name
        self.account_no = account_no
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You have deposited {amount} your balance is {self.balance}")
        else:
            print("the deposit amount must be positive")
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"your withdrwal request of {amount} was successful. Your new balance is {self.balance}")        
        else:
            print("You have insufficient funds")
    def display_balance(self):
        print(f"{self.account_name}'s balance is {self.balance}")

class equity(bank_account):
    pass
class liability(bank_account):
    pass

equity = bank_account("Anne", 1357, 20000)
liability = liability("Lucy", 2468, 11000)

equity.display_balance()
liability.display_balance()

equity.deposit(3000)
liability.withdraw(5000)