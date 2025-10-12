# bank_account.py

class BankAccount:
    """A simple bank account class to handle deposits, withdrawals, and balance display."""

    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if funds are sufficient."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False  # Not enough funds

    def display_balance(self):
        """Print the current balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
