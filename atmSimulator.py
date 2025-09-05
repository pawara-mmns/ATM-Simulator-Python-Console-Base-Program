import os

# ===== Function to Clear Console =====
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# ===== Data Arrays =====
account_numbers = [1001, 1002, 1003]   # Account Numbers
pins = [1234, 2345, 3456]              # PINs
names = ["Kamal", "Nimal", "Sunil"]    # User names
balances = [5000, 10000, 7500]         # Balances (in Rs)


# ===== ATM Functions =====
def authenticate(account, pin):
    if account in account_numbers:
        index = account_numbers.index(account)
        if pins[index] == pin:
            return index
    return -1


def check_balance(index):
    print(f"Your current balance is: Rs {balances[index]}")


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


# ===== Main Program =====
print("💳 Welcome to the ATM Simulator 💳")

account = int(input("Enter your account number: "))
pin = int(input("Enter your PIN: "))

user_index = authenticate(account, pin)

if user_index != -1:
    print(f"Login successful! Welcome {names[user_index]} 🙏")

    while True:
        clear_console()
        print("\n===== ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Change PIN")
        print("6. View Account Details")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(user_index)
        elif choice == "2":
            deposit(user_index)
        elif choice == "3":
            withdraw(user_index)
        elif choice == "4":
            transfer(user_index)
        elif choice == "5":
            change_pin(user_index)
        elif choice == "6":
            user_details(user_index)
        elif choice == "7":
            print("Thank you for using the ATM. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

        # Ask before going back to menu
        back = input("\nDo you want to go back to main menu? (y/n): ")
        if back.lower() != "y":
            print("Thank you for using the ATM. Goodbye! 👋")
            break

else:
    print("Authentication failed ❌ Invalid account number or PIN.")
