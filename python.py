from unicodedata import name


class User:
    def __init__(self,name):
        self.name = name
        self.amount = 200000

    def make_withdrawal(self,amount):
        self.amount -=amount

    def make_deposit(self,amount):
        self.amount +=amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        self.amount += amount
        self.display_user_balance()


jp = User('Jp')
monica = User('Monica')
lenny = User('Lenny')

jp.make_withdrawal(80000)
jp.make_deposit(5000)
jp.make_deposit(150000)
jp.make_deposit(34000)
jp.display_user_balance()

monica.make_deposit(40)
monica.make_withdrawal(35)
monica.display_user_balance()

lenny.make_deposit(120)
lenny.make_withdrawal(200)
lenny.make_deposit
lenny.display_user_balance()

monica.transfer_money(700, jp)
