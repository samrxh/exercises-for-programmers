def password_strength(password):
    # checks string for the following traits and returns strength of password
    # -2: very weak, -1: weak, 0: (>8 letters), 1: (<8 special ch), 2: strong, 3: very strong
    ch_count = len(password) >= 8
    only_numbers = password.isnumeric()
    only_alpha = password.isalpha()
    has_number = any(digit in password for digit in '0123456789')
    has_special = not password.isalnum()
    strength = 0
    if ch_count:
        strength += 1
    if only_numbers:
        strength -= 3
    if only_alpha:
        strength -= 1
    if has_number:
        strength += 1
    if has_special:
        strength += 1
    return strength


def password_checker(password):
    # takes in password, finds strength, returns string
    strength = password_strength(password)
    if strength == -2:
        strength = 'very weak'
    elif -1 <= strength <= 1:
        strength = 'weak'
    elif strength == 2:
        strength = 'strong'
    elif strength == 3:
        strength = 'very strong'
    return print(f"The password '{password}' is a {strength} password.")


print("Password checker. Type 'q' to exit.")
while True:
    pwd = input("What is your password? ")
    if pwd == 'q':
        break
    password_checker(pwd)
