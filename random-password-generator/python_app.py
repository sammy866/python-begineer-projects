# Ask user if they want to generate a password or not
# If yes, ask for password length
# Generate password
# Print password
# If initial response is no, exit program

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$&*()")


def generate_password():
    password_length = int(
        input("How long would you like your password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(f"Your new password is: {password}\n")


while True:
    option = input("Do you want to generate a password? (Yes/No) ")

    if option == "Yes":
        generate_password()
    elif option == "No":
        print("Goodbye")
        break
    else:
        print("Invalid input, please enter Yes or No.\n")
