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
        print(f"Remaining Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for all_accounts in cls.all_accounts:
            all_accounts.display_account_info()

account_1 = BankAccount(.02, 5000)
account_2 = BankAccount(.07, 7500)

account_1.deposit(200).deposit(500).deposit(300).withdraw(500).yield_interest().display_account_info()
account_2.deposit(100).deposit(500).withdraw(1500).withdraw(200).withdraw(150).withdraw(150).yield_interest().display_account_info()

BankAccount.print_all_accounts()

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(0.5,0)

    def make_deposit(self, amount):
        self.account += amount
        return self

    def make_withdrawal(self, amount):
        self.account -= amount
        return self

    def display_user_balance(self):
        print(f"User : {self.name}, Balance : {self.account}")
        return self

    def transfer_money(self, user, amount):
        self.account -= amount
        user.account += amount
        print(self.display_user_balance(), "**After Transfer(Sent)**\n")
        print(user.display_user_balance(), "**After Transfer(Recieved)**\n")

alex = User("Alex Fernandez", "afpato3@gmail.com")
manuel = User("Manuel Felix", "mannyf@outlook.com")
jacob = User("Jacob Reyes", "jreyes@outlook.com")

alex.account.deposit(700).withdraw(100).yield_interest().display_account_info()