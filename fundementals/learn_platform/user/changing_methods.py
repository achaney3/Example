class User:
    def __init__(self, name, email, account_balance):
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
        return self

sonny = User('Sonny','sonny@email.com', 0)
bobby = User('Bobby','heybobby@email.com',10)
josh = User('Joshua', 'joshy@email.com', 50)
sonny.display_user_balance()
bobby.display_user_balance()
josh.display_user_balance()

sonny.make_deposit(50).make_deposit(50).make_deposit(300).make_withdrawal(25).display_user_balance()

bobby.make_deposit(200).make_deposit(100).make_withdrawal(30).make_withdrawal(10).display_user_balance()

josh.make_deposit(5).make_withdrawal(1).make_withdrawal(1).make_withdrawal(1).display_user_balance()

bobby.transfer_money(josh,70).display_user_balance()
josh.display_user_balance()