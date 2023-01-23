# original variant
# try:
#     people = int(input("How many people? "))
#     pizzas = int(input("How many pizzas? "))
#     slices = int(input("How many slices per pizza? "))
#     total_slices = pizzas * slices
#     portion = total_slices // people
#     leftover = total_slices % people
#     p_slices = 'slice' if portion == 1 else 'slices'
#     l_slices = 'slice' if leftover == 1 else 'slices'
#     print(f'Everyone gets {portion} {p_slices} of pizza. There will be {leftover} {l_slices} leftover.')
# except ValueError:
#     print("You must enter a number.")

# how many pizzas variant
import math


def pizzas_needed(people, wanted, slices):
    pizzas = int(math.ceil((people * wanted) / slices))
    total_slices = pizzas * slices
    portion = total_slices // people
    leftover = total_slices % people
    return portion, leftover, pizzas


try:
    input_people = int(input("How many people? "))
    input_wanted = int(input("How many slices do people want? "))
    input_slices = int(input("How many slices per pizza? "))
    output_portion, output_leftover, output_pizzas = pizzas_needed(input_people, input_wanted, input_slices)
    p_slices = 'slice' if output_portion == 1 else 'slices'
    l_slices = 'slice' if output_leftover == 1 else 'slices'
    print(f"You will need to purchase {output_pizzas} pizzas.")
    print(f'Everyone gets {output_portion} {p_slices} of pizza. There will be {output_leftover} {l_slices} leftover.')
except ValueError:
    print("You must enter a number.")
