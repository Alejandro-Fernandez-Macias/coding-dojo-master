class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds : Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Remaining Balance: ${self.balance}\n")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for all_accounts in cls.all_accounts:
            all_accounts.display_account_info()

Account_1 = BankAccount(.02, 5000)
Account_2 = BankAccount(.07, 7500)

Account_1.deposit(200).deposit(500).deposit(300).withdraw(500).yield_interest().display_account_info()
Account_2.deposit(100).deposit(500).withdraw(1500).withdraw(200).withdraw(150).withdraw(150).yield_interest().display_account_info()

BankAccount.print_all_accounts()