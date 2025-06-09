class BankAccount:
    def __init__(self, name, amount, interest_rate):
        self.name = name  
        self.amount = amount  
        self.interest_rate = interest_rate
    def apply_interest(self):
        interest = (self.amount * self.interest_rate) / 100
        self.amount = self.amount+interest


account = BankAccount("Python ALC", 1000, 6.78)
account.apply_interest()
print("Account Holder Name:",account.name)
print("Balance after applying interest rate",account.interest_rate,"%","is",account.amount,"Rs")

account.interest_rate = 9.35
account.apply_interest()
print("Balance after applying interest rate ",account.interest_rate,"%","is",account.amount,"Rs")
