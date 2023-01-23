legal_ages = {'The United States': 16, 'Mexico': 15, 'Japan': 18}
age = int(input("What is your age? "))
legal_countries = [key for key, value in legal_ages.items() if value <= age]
if not legal_countries:
    print("You are not able to legally drive.")
elif len(legal_countries) == 1:
    print(f"You are able to legally drive in {legal_countries[0]}.")
else:
    legal_countries_last = legal_countries.pop()
    print(f"You are able to legally drive in {', '.join(legal_countries)} and {legal_countries_last}.")
