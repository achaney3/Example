class BankAccount:
        accounts = []
        def __init__(self, int_rate=0, balance=0):
                self.int_rate = int_rate
                self.balance = balance
                BankAccount.accounts.append(self)
        def deposit(self, amount):
                self.balance += amount
                return self
        def withdraw(self, amount):
                if(self.balance - amount) >=0:
                        self.balance -= amount
                else:
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
        @classmethod
        def print_accounts(cls):
                for account in cls.accounts:
                        account.display_account_info()
class User:
        def __init__(self, name ):
                self.name = name
                self.account = {
                        "checking" : BankAccount(int_rate =0.07, balance=100),
                        "savings" : BankAccount(int_rate=.05, balance=300)}

        def make_deposit(self,amount):
                self.account.deposit(30)
                return self

        def make_withdrawal(self,amount):
                self.account.withdraw(10)
                return self

        def display_user_balance(self):
                print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
                print(f"User: {self.name}, Savings  Balance: {self.account['savings'].display_account_info()}")
                return self
        def transfer_money(self,amount,user):
                self.amount -= amount
                user.amount += amount
                self.display_user_balance()
                user.display_user_balance()
                return self


mia = User("Mia")

mia.account['checking'].deposit(25)
mia.display_user_balance()