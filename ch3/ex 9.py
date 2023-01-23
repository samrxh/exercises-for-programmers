import math

PI = math.pi
COVERAGE = 350


def calculate_gallons():
    try:
        length = int(input("Length: "))
        width = int(input("Width: "))
        area = length * width
        print(f'{area} square feet: area of room.')
        needed_gals = math.ceil(area / COVERAGE)
        print(f'{needed_gals} gallons needed to cover this area.')
    except ValueError:
        print("Please enter a number.")


def calculate_round_gallons():
    try:
        length = int(input("Length: "))
        width = int(input("Width: "))
        area = round((length / 2) * (width / 2) * PI, 1)
        print(f'{area} square feet: area of round room.')
        needed_gals = math.ceil(area / COVERAGE)
        print(f'{needed_gals} gallons needed to cover this area.')
    except ValueError:
        print("Please enter a number.")


def calculate_l_gallons():
    length1 = int(input("Length 1: "))
    width1 = int(input("Width 1: "))
    length2 = int(input("Length 2: "))
    width2 = int(input("Width 2: "))
    length = max(length1, length2)
    width = max(width1, width2)
    area = length * width
    print(f'{area} square feet: area of longest sides.')
    length_cut = abs(length1 - length2)
    width_cut = abs(width1 - width2)
    area_cut = length_cut * width_cut
    print(f'{area_cut} square feet: area of shorter sides.')
    area -= area_cut
    print(f'{area} square feet: area of L shape.')
    needed_gals = math.ceil(area / COVERAGE)
    print(f'{needed_gals} gallons needed to cover this area.')


calculate_round_gallons()
