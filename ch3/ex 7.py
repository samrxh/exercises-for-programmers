def area_conversion(system, length, width):
    conversion_factor = 0.09290304
    if system == 'f':
        try:
            square_feet = round(length * width, 3)
            square_meters = round(square_feet * conversion_factor, 3)
            # I know you're not supposed to print in a function but I'm still gonna do it.
            print(f"You entered the dimensions {length} feet by {width} feet.")
            print(f"The area is \n{square_feet} square feet.\n{square_meters} square meters.")
        except ValueError:
            print("You must enter a number.")
            exit()
    elif system == 'm':
        try:
            square_meters = round(length * width, 3)
            square_feet = round(square_meters / conversion_factor, 3)
            print(f"You entered the dimensions {length} meters by {width} meters.")
            print(f"The area is \n{square_feet} square feet.\n{square_meters} square meters.")
        except ValueError:
            print("You must enter a number.")
            exit()
    else:
        print("Please enter 'f' or 'm'.")


input_system = input("Enter 'f' to use feet or 'm' to use meters. ")
input_length = int(input("What is the length? "))
input_width = int(input("What is the width? "))
area_conversion(input_system, input_length, input_width)
