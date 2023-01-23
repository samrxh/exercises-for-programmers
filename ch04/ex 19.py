# prompt for height and weight
height = int(input("What is your height in inches? "))
weight = int(input("What is your weight in pounds? "))

# calculate BMI
bmi = (weight / (height * height)) * 703

# if BMI between 18.5 and 25, print normal weight
# if out of that range, under or over weight
if 18.5 < bmi < 25:
    print(f"{bmi}: Normal weight range.")
elif bmi < 18.5:
    print(f"{bmi}: Underweight")
elif 25 < bmi:
    print(f"{bmi}: Overweight")
