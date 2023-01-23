def calculate_simple_interest(principal, interest_rate, compound, years):
    for year in range(years):
        amount = round(principal * (1 + (interest_rate / compound)) ** (compound * (year + 1)), 2)
        yield amount


principal = int(input("Enter the principal: "))
interest_rate = float(input("Enter the rate of interest: ")) / 100
years = int(input("Enter the number of years: "))
compound = int(input("Enter the number of times the interest is compounded per year: "))

amount = calculate_simple_interest(principal, interest_rate, compound, years)
for item in enumerate(amount):
    print(f'After {item[0] + 1} year(s), your investment will be worth ${item[1]}')
