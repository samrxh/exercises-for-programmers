# tip calculator exercise
def calculator(bill, tip_percent):
    # takes bill amount and tip percent, spits out tip amount and total
    try:
        bill = float(bill)
        if bill <= 0:
            print("Please type an amount greater than zero.")
    except ValueError:
        print("Please type a number.")
    try:
        tip_percent = float(tip_percent)
        if tip_percent <= 0:
            print("Please type an amount greater than zero.")
    except ValueError:
        print("Please type a number.")
    tip = round(bill * (tip_percent / 100), 2)
    total = round(bill + tip, 2)
    return tip, total


while True:
    bill = input("What is the total of the bill? ")
    tip_percent = input("What percentage would you like to tip? ")
    tip, total = calculator(bill, tip_percent)
    print(f"The tip amount is: ${tip}")
    print(f"The total amount is: ${total}")
