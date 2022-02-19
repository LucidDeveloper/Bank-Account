'''
@ author:
Gianni M. Javier
'''
# Create a BankAccount class with the attributes interest rate 
# and balance

# Ninja Bonus
# Initiate variable with empt list to store bank account info
all_bank_accounts_info = []

# BankAccount class
class BankAccount: 
    # Constructor using Special Method init
    def __init__(self,interest_rate = 0.01,account_balance = 0): # Instance Constructor upon Instantiation
        self.interest_rate = interest_rate
        self.account_balance = account_balance
        all_bank_accounts_info.append(self)
        
# Instance Methods

# Add a deposit method to the BankAccount class
# deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.account_balance += amount
        return self

# Add a withdraw method to the BankAccount class
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self,amount):
        self.account_balance -= amount
        return self

# Add a display_account_info method to the BankAccount class
# display_account_info(self) - print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print(f'Account Balance: {self.account_balance}')
        return self

# Add a yield_interest method to the BankAccount class  
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance = self.account_balance + (self.account_balance * self.interest_rate)
        return self

#NINJA BONUS:
# Print all instances of a Bank Account's info
    @classmethod
    def print_all_bank_accounts_info(cls):
        for bank_account in all_bank_accounts_info:
            bank_account.display_account_info()
        return cls

# Create 2 accounts
account_gmj = BankAccount(0.05,50000)
account_aa = BankAccount(0.06,60000)

# To the first account, make 3 deposits and 1 withdrawal, 
# then yield interest and display the account's info 
# all in one line of code (i.e. chaining)

account_gmj.deposit(10000).deposit(5000).deposit(5000).withdraw(2500).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals,
# then yield interest and display the account's info 
# all in one line of code (i.e. chaining)

account_aa.deposit(10000).deposit(10000).withdraw(2500).withdraw(2500).withdraw(1250).withdraw(1250).yield_interest().display_account_info()

# NINJA BONUS: use a classmethod to print all instances of a 
# Bank Account's info

BankAccount.print_all_bank_accounts_info()