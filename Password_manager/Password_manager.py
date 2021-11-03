from cryptography.fernet import Fernet

''' Run only first time to generate the key. For a new key, file "Passwords.key" must be cleared '''
# def create_key():
#     key = Fernet.generate_key()
#     with open('key.key', 'wb') as key_file:
#         key_file.write(key)
# create_key()


def read_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


key = read_key()    # reads the decrypting key from the file
fer = Fernet(key)

def add_pass():
    account = input("Account Name: ")
    acc_pwd = input("Password: ")
    with open('passwords.key', 'a') as key_file:
        key_file.write(account + '|' + fer.encrypt(acc_pwd.encode()).decode() + '\n')
        print("Information has been saved!")
    return


def view_pass():
    print("Here are the current accounts and corresponding passwords:")
    with open('passwords.key', 'r') as key_file:
        for line in key_file.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print('Username: ', user, ' | Password: ', fer.decrypt(pwd.encode()).decode())


while True:
    user_input = input('Would you like to add a new password or view '
                       'the saved ones (add, view or q to exit the program)? ').lower()
    if user_input == 'q':
        quit(0)
    elif user_input == 'add':
        add_pass()
    elif user_input == 'view':
        view_pass()
    else:
        print("This option does not exist, please try again")
