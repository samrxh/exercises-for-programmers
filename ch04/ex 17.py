alcohol_consumed = int(input("How much alcohol have you consumed? "))
body_weight = int(input("How much do you weigh? "))
if input("What is your sex? ") == 'm':
    gender = .73
else:
    gender = .66
hours = int(input("How many hours has it been? "))
bac = (alcohol_consumed * 5.14 / body_weight * gender) - .015 * hours
print(bac)
if bac >= .08:
    print("It is not legal for you to drive.")
else:
    print("It is legal for you to drive.")
