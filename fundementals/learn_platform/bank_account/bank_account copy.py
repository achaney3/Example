class BankAccount:
        def __init__(self, name, int_rate=0, balance=0):
                self.name = name
                self.int_rate = int_rate
                self.balance = balance
        def deposit(self, amount):
                self.balance += amount
                return self
        def withdraw(self, amount):
                self.balance -= amount
                if self.balance == 0:
                        print("Insufficient funds: You will be charged a $5 fee")
                        self.balance -= 5   
                return self     
        def display_account_info(self):
                print(f'Balance is: {self.balance}')
                return self
        def yield_interest(self):
                if self.balance >0:
                        self.balance += self.balance * self.int_rate
                return self
class User:
        def __init__(self, name ):
                self.name = name
                self.account = BankAccount(int_rate =0.07)

        def make_deposit(self,amount):
                self.account.deposit(30)
                return self

        def make_withdrawal(self,amount):
                self.account.withdraw(10)
                return self

        def display_user_balance(self):
                print(self.account.balance)
                return self


mia = User("Mia")
joe = BankAccount("Joe")

mia.make_deposit(30).make_deposit(20).make_deposit(25).make_withdrawal(10).display_user_balance()

joe.deposit(50).deposit(100).withdraw(10).withdraw(15).withdraw(10.).withdraw(5).yield_interest().display_account_info()