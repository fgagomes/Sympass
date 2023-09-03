from encryption import encrypt, decrypt
import os
import string
import random
import pyperclip


def check_credentials(username):
    username += ".txt"
    file = open(username, "a")
    if os.stat(username).st_size != 0:  # If the file exists and is not empty

        file = open(username, "r")
        line = file.readline()  # This first line is the stored master password

        password = input("Enter your password: ")
        
        if (encrypt(password) + "\n") == line:  # If password corresponds to first line of the file
            file.close()
            return True
        else:
            file.close()
            return False
    else:  # If the file doesn't exist or is empty, this will create the file and ask for master password, then store it
        file = open(username, "a")
        password = input("New user. Create your password: ")
        file.write(encrypt(password) + "\n")
        file.close()
        username = username[:-4]
        main_screen(username)


def main_screen(username):

    action = input(f"What do you wish to do?\n\n"
                   f"1 - Create new password\n"
                   f"2 - Check stored passwords\n"
                   f"3 - Exit\n"
                   f"Your choice: ")

    match action:
        case "1":
            create_pass(username)
            main_screen(username)
        case "2":
            check_pass(username)
            main_screen(username)
        case "3":
            exit()
        case _:
            print(f"\nInvalid choice. Try again.")
            main_screen(username)


def create_pass(username):

    service = input("What service is this password for? ")
    credential = input("What is the username for this service? ")

    # Ensure that password has at least 1 uppercase, 1 digit and 1 special character:
    password = random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    characters = string.ascii_letters + string.digits + string.punctuation
    password += ''.join(random.choice(characters) for i in range(10))

    # Convert password to list, shuffle the list content and turn it back into a string
    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)

    # This will automatically copy new password to clipboard
    pyperclip.copy(password)
    print(f"Your password is: {password} (copied to clipboard)\n\n")

    # This will store the data in the file encrypting values, so it's not easily readable
    username += ".txt"
    file = open(username, "a")
    file.write(encrypt(service) + "\t" + encrypt(credential) + "\t" + encrypt(password) + "\n")
    file.close()


def check_pass(username):

    username += ".txt"
    file = open(username, "r")
    line = file.readline()  # This first line is the user master password, should be ignored
    line = file.readlines()  # The remaining lines contain the stored information
    for i, block in enumerate(line):  # Each line = block of values for Service-Username-Password, separated by "\t"
        value = block.split("\t")

        print(f"Entry {i+1}\n"
              f"Service:\t{decrypt(value[0])}\n"
              f"Username:\t{decrypt(value[1])}\n"
              f"Password:\t{decrypt(value[2])}")
    file.close()
