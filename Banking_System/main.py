from user import User
from bank import Bank
from interface import data

def is_valid(value):
    options = [1, 2, 3, 4, 5]
    if value.isdigit():
        value = int(value)
        if value in options:
            return True, value
    return "Invalid option."

def is_valid_value(value):
    if value.isdigit():
        value = int(value)
        return True
    return "Invalid amount."




if __name__ == "__main__":
    b = Bank("Vasil", 'Vasilev', 'Sofia', 1234567890)
    print(data[0])
    while True:
        print('')
        PIN = input('Please enter your PIN or type "Finish" to exit: ')
        if PIN == 'Finish':
            quit(121)
        elif PIN.isdigit():
            PIN = int(PIN)
            if PIN == 3520:
                print(b.user_info())
            else:
                print('Incorrect PIN, please try again.')
        else:
            print("The PIN should contain numbers only, please try again.")
        break
while True:
    print(data[1])
    option = input('Please choose an option: ')
    result, number = is_valid(option)
    if result == True:
        if number == 1:
            print(b.user_info())
        elif number == 2:
            b.add_account()
        elif number == 3:
            amt = input("Amount of money to deposit: ")
            res = is_valid_value(amt)
            if res == True:
                b.deposit(int(amt))
            else:
                print(res)

        elif number == 4:
            amt = input("Amount of money to withdraw: ")
            res = is_valid_value(amt)
            if res == True:
                b.withdrawal(int(amt))
            else:
                print(res)
        else:
            quit(121)
    else:
        print(result)

