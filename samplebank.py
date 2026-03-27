import json

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = float(balance)
        self.transactions = []

    def deposit(self, amount):
        amount = float(amount)
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited {amount}")
            print("✅ Deposit successful")
        else:
            print("❌ Invalid amount")

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            print("✅ Withdrawal successful")
        else:
            print("❌ Insufficient balance")

    def show_balance(self):
        print(f"💰 Balance: {self.balance}")

    def show_transactions(self):
        print("📜 Transactions:")
        for t in self.transactions:
            print("-", t)

    def to_dict(self):
        return {
            "name": self.name,
            "balance": self.balance,
            "transactions": self.transactions
        }


class Bank:
    def __init__(self, file="bank.json"):
        self.file = file
        self.accounts = self.load_accounts()

    def load_accounts(self):
        try:
            with open(self.file, "r") as f:
                data = json.load(f)
                accounts = {}
                for name, info in data.items():
                    acc = Account(name, info["balance"])
                    acc.transactions = info["transactions"]
                    accounts[name] = acc
                return accounts
        except:
            return {}

    def save_accounts(self):
        data = {name: acc.to_dict() for name, acc in self.accounts.items()}
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def create_account(self, name):
        if name in self.accounts:
            print("❌ Account already exists")
        else:
            self.accounts[name] = Account(name)
            self.save_accounts()
            print("✅ Account created")

    def get_account(self, name):
        return self.accounts.get(name, None)


def main():
    bank = Bank()

    while True:
        print("\n--- Banking System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transactions")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Enter name: ")
            bank.create_account(name)

        elif choice in ["2", "3", "4", "5"]:
            name = input("Enter account name: ")
            acc = bank.get_account(name)

            if not acc:
                print("❌ Account not found")
                continue

            if choice == "2":
                amount = input("Amount: ")
                acc.deposit(amount)

            elif choice == "3":
                amount = input("Amount: ")
                acc.withdraw(amount)

            elif choice == "4":
                acc.show_balance()

            elif choice == "5":
                acc.show_transactions()

            bank.save_accounts()

        elif choice == "6":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()