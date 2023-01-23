choice = input("""Press C to convert from Fahrenheit to Celsius.
Press F to convert from Celsius to Fahrenheit.
Your choice: """).lower()
answer = 0

if choice == 'c':
    unit = 'Celsius'
    temp = int(input(f"Please enter the temperature in Fahrenheit: "))
    answer = (temp - 32) * 5/9
else:
    unit = 'Fahrenheit'
    temp = int(input(f"Please enter the temperature in Celsius: "))
    answer = (temp * 9/5) + 32

print(f"The temperature in {unit} is {answer}.")
