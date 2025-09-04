import os

# Data Arrays 
account_numbers = [1001, 1002, 1003]   # Account Numbers
pins = [1234, 2345, 3456]              # PINs
names = ["Kamal", "Nimal", "Sunil"]    # User names
balances = [5000, 10000, 7500]         # Balances 
# changepins = [1111, 2222, 3333]        # Change PINs

#  ATM Functions
def authenticate(account, pin):
    if account in account_numbers:
        index = account_numbers.index(account)
        if pins[index] == pin:
            return True
        return-1
        
def check_balance(index):
    print(f"Your Current balance is {balances[index]}")


