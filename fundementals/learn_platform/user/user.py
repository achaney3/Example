# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class User:
    def __init__(self, name, email,account_balance=0):
        self.name = name
        self.email = email
        self.account_balance = account_balance

    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self, other_user

sonny = User('Sonny','sonny@email.com')
bobby = User('Bobby','heybobby@email.com',10)
josh = User('Joshua', 'joshy@email.com', 50)
sonny.display_user_balance()
bobby.display_user_balance()
josh.display_user_balance()

sonny.make_deposit(50)
sonny.make_deposit(50)
sonny.make_deposit(300)
sonny.make_withdrawal(25)
sonny.display_user_balance()

bobby.make_deposit(200)
bobby.make_deposit(100)
bobby.make_withdrawal(30)
bobby.make_withdrawal(10)
bobby.display_user_balance()

josh.make_deposit(5)
josh.make_withdrawal(1)
josh.make_withdrawal(1)
josh.make_withdrawal(1)
josh.display_user_balance()

bobby.transfer_money(sonny,70)
sonny.display_user_balance()
bobby.display_user_balance()