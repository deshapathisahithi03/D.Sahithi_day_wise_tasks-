# Check balance
def check_balance(balance):
    print(f"Your balance is: {balance}")
# Deposit money
def deposit(balance):
    amount = float(input("How much would you like to deposit?"))
    if amount > 0:
        balance += amount
        print(f"You deposited: {amount}. New balance: {balance}")
    else:
        print("Please enter a valid amount.")
    return balance
# Withdraw money
def withdraw(balance):
    amount = float(input("How much would you like to withdraw? $"))
    if amount > balance:
        print("You don't have enough balance to withdraw that amount.")
    elif amount <= 0:
        print("Please enter a valid amount.")
    else:
        balance -= amount
        print(f"You withdrew {amount}. New balance: {balance}")
    return balance

# Main function
def main():
    balance = 0.0
    while True:
        print("\n Welcome to the ATM")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Thank you for using the ATM. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# calling the main function to start the process
main()
