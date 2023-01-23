def years_to_double():
    while True:
        try:
            rate = int(input("What is the rate of return? "))
            years = 72 / rate
        except ValueError:
            print("Your input must be a number.")
            continue
        except ZeroDivisionError:
            print("Your input must not be 0.")
            continue
        return round(years)


ytd = years_to_double()
print(f"It will take {ytd} years to double your initial investment.")
