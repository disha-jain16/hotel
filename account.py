class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def display_balance(self):
        print(f"{self.owner}'s balance: ${self.balance}")

# Test
acc = BankAccount("Alice", 100)
acc.deposit(50)
acc.withdraw(30)
acc.display_balance()  # Output: Alice's balance: $120
