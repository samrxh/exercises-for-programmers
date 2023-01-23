import time
current_year = time.localtime().tm_year


def retire(age, retirement_age):
    years_left = retirement_age - age
    can_retire = False
    if years_left < 0:
        can_retire = True
    return can_retire, years_left


input_age = int(input('What is your current age? '))
input_retirement_age = int(input('What age would you like to retire? '))
retire_result, years_left_result = retire(input_age, input_retirement_age)
if retire_result is True:
    print("You can retire now!")
else:
    print(f'You have {years_left_result} years left until you can retire.')
    print(f"It's {current_year}, so you can retire in {current_year + years_left_result}.")
