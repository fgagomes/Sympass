Name: Felipe Galvao de Andrade Gomes
ID: 2310779

Project Sympass

A simple program for strong password creation and storage.

Features:

1. Ask for username
    1.1. Creates new user if username not detected
    1.2. Creates a file and stores password for new user
    1.3. If user exists, ask for main password to be accessed

2. Ask if user wants to create new password or access existing ones

3. Create new password:
    3.1. Ask for service and login information from user
    3.2. Create a strong password and show it to user
    3.3. Automatically copy password to clipboard
    3.4. Encrypt the information
    3.5. Store encrypted information in a file

4. Show decrypted content of the file to user upon demand


Files:

1) main.py
Prints welcome page and runs function check_credentials().

2) functionalities.py
Contains the basic functions of the program:
check_credentials(): grant access with password or create new user
main_screen(): shows options to user
create_pass(): creates a new password for user
check_pass(): shows stored passwords to user

3) encryption.py
Contains the encrypt() and decrypt() functions, used by the other functions to store and read data.
Note: They use a simple base64 encoding, which is not secure enough and should be updated in later versions.
These functions should be updated when my knowledge of encryption is better.

4) requirements.txt
Contains required packages


References:

https://stackoverflow.com/questions/2507808/how-to-check-whether-a-file-is-empty-or-not

https://stackoverflow.com/questions/56381066/how-to-open-a-file-in-both-read-and-append-mode-at-the-same-time-in-one-variable

https://www.guru99.com/python-file-readline.html

https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/

https://pynative.com/python-generate-random-string/

https://realpython.com/python-enumerate/

https://stackoverflow.com/questions/11063458/python-script-to-copy-text-to-clipboard

https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/

https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/