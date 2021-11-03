class User:

    def __init__(self, first_name, last_name, city, account):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.account = account

    def user_info(self):
        return f'{self.first_name} {self.last_name}\n{self.city}\nAccount {self.account}'

