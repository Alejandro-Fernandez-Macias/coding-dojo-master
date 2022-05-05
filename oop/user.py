class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User : {self.name}, Balance : {self.account_balance}")
        return self

    def transfer_money(self, user, amount):
        self.account_balance -= amount
        user.account_balance += amount
        print(self.display_user_balance(), "**After Transfer(Sent)**\n")
        print(user.display_user_balance(), "**After Transfer(Recieved)**\n")

alex = User("Alex Fernandez", "afpato3@gmail.com")
manuel = User("Manuel Felix", "mannyf@outlook.com")
jacob = User("Jacob Reyes", "jreyes@outlook.com")
# print(alex.name)
# print(manuel.name)
# print(jacob.name)

alex.make_deposit(100).make_deposit(200).make_deposit(200).make_withdrawal(100).display_user_balance()

manuel.make_deposit(500).make_deposit(150).make_withdrawal(200).make_withdrawal(150).display_user_balance()

jacob.make_deposit(750).make_withdrawal(250).make_withdrawal(175).make_withdrawal(150).display_user_balance()

alex.transfer_money(jacob, 250)
