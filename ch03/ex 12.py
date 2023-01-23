def calculate_simple_interest(principal, interest_rate, years):
    for year in range(years):
        amount = round(principal * (1 + interest_rate * (year + 1)), 2)
        yield amount


principal = int(input("Enter the principal: "))
interest_rate = float(input("Enter the rate of interest: ")) / 100
years = int(input("Enter the number of years: "))
amount = calculate_simple_interest(principal, interest_rate, years)
for item in enumerate(amount):
    print(f'After {item[0] + 1} year(s), your investment will be worth ${item[1]}')
# print(f"After {years} years at {interest_rate * 100}%, the investment will be worth ${amount}")
