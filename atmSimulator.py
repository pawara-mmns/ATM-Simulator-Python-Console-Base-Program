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

def deposit(index):
    amount = float(input("Enter amount to deposit (Rs): "))
    if amount > 0:
        balances[index] += amount
        print(f"Deposit successful! New balance: Rs {balances[index]}")
    else:
        print("Invalid deposit amount.")


def withdraw(index):
    amount = float(input("Enter amount to withdraw (Rs): "))
    if 0 < amount <= balances[index]:
        balances[index] -= amount
        print(f"Withdrawal successful! New balance: Rs {balances[index]}")
    else:
        print("Insufficient balance or invalid amount.")


def transfer(index):
    target_acc = int(input("Enter target account number: "))
    if target_acc in account_numbers:
        amount = float(input("Enter amount to transfer (Rs): "))
        if 0 < amount <= balances[index]:
            target_index = account_numbers.index(target_acc)
            balances[index] -= amount
            balances[target_index] += amount
            print(f"Transfer successful! Your new balance: Rs {balances[index]}")
        else:
            print("Insufficient balance or invalid amount.")
    else:
        print("Target account not found.")


def change_pin(index):
    old_pin = int(input("Enter current PIN: "))
    if old_pin == pins[index]:
        new_pin = int(input("Enter new PIN: "))
        pins[index] = new_pin
        print("PIN changed successfully!")
    else:
        print("Incorrect current PIN.")


def user_details(index):
    print("===== Account Details =====")
    print("Account Number:", account_numbers[index])
    print("Account Holder:", names[index])
    print(f"Balance: Rs {balances[index]}")