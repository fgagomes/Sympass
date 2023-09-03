from functionalities import check_credentials, main_screen
from encryption import encrypt, decrypt


def main():
    print("Welcome to Sympass - a (very) simple password creator")
    username = input("Enter your username: ")
    username = encrypt(username)

    if check_credentials(username):  # If the credentials are correct, return will be True
        print(f"\nWelcome, _{decrypt(username)}_.")
        main_screen(username)
    else:
        for i in range(2):
            print("Wrong password. Try again")
            check_credentials(username)
        else:
            print("You typed a wrong password three times, program terminated.")
            exit()


if __name__ == '__main__':
    main()
