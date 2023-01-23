import string
from random import choice, shuffle


def password_generator(length, punctuation, numbers):
    letters_ls = []
    symbols_ls = []
    numbers_ls = []
    for item in range(length - punctuation - numbers):
        letters_ls.append(choice(string.ascii_letters))
    for item in range(punctuation):
        symbols_ls.append(choice(string.punctuation))
    for item in range(numbers):
        numbers_ls.append(choice(string.digits))
    password = letters_ls + symbols_ls + numbers_ls
    shuffle(password)
    password = ''.join(password)
    return password


try:
    user_length = int(input("What's the minimum length? "))
    user_punctuation = int(input("How many special characters? "))
    user_numbers = int(input("How many numbers? "))
    user_options = int(input("How many options would you like? "))
    passwords = [password_generator(user_length, user_punctuation, user_numbers) for password in range(user_options)]
    passwords = '\n'.join(passwords)
    print(f"Your password options are...\n{passwords}")
except ValueError:
    print("You must enter a number.")

# challenge: place the password on the user's clipboard when generated. this can be done with tkinter
