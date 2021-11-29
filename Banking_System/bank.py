from user import User
from collections import defaultdict


class Bank(User):
    def __init__(self, first_name, last_name, city, account):
        super().__init__(first_name, last_name, city, account)
        self.account = account
        self.balance = 0
        self.user_accounts = defaultdict(lambda: None)

    def account_balance(self):
        return f' <<< Your current balance is ${self.balance} >>>'

    def withdrawal(self, amount):
        if self.balance < amount:
            print(f'Insufficient funds!')
            print(self.account_balance())
            print('*******************************')
            return
        elif amount < 10:
            print('Minimum amount to withdraw is $10.')
            return
        self.balance -= amount
        print(f'{amount} was withdrawn from your account ending with ******{str(self.account)[-4:]}')
        print(self.account_balance())
        print('*******************************')

    def deposit(self, amount):
        print(f' - ${amount} was added to your account!')
        self.balance += amount
        print(self.account_balance())
        print('*******************************')

    def add_account(self):
        new_account = input('Please provide your account number: ')
        new_account_alias = input('Please provide a name for your account: ')
        if new_account_alias in self.user_accounts:
            print(f'Account {new_account} is already added.')
            return
        self.user_accounts[new_account_alias] = new_account
