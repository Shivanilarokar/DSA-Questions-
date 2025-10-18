class BankAccount:
    """OOP example for managing a simple bank account."""
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"💰 Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient funds")
        else:
            self.balance -= amount
            print(f"💸 Withdrawn: {amount}")

    def show_balance(self):
        print(f"Account Balance for {self.owner}: ₹{self.balance}")

# Example
# acc = BankAccount("Shivani", 5000)
# acc.deposit(1000); acc.withdraw(2000); acc.show_balance()
