# main-0.py
import sys
from bank_account import BankAccount

def main():
    # Create a new account with a starting balance of $100
    account = BankAccount(100)

    # Check if the user provided a command
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse command (like "deposit:50" -> command=deposit, amount=50)
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Handle each command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")

    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")

    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command. Try: deposit:<amount>, withdraw:<amount>, or display")

if __name__ == "__main__":
    main()
