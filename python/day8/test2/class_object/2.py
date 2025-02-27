class BankAccount:
    def __init__(self, account_holder: str, balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            print(" Withdrawal denied due to low balance")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
    
    def get_balance(self) -> float:
        return self.balance

# Example usage
account = BankAccount("Arun", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200)  # Should prevent overdraft
print(f"Final Balance: {account.get_balance()}")
