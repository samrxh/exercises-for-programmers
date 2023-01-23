order_amount = int(input("What is the order amount? "))
total = order_amount
state = input("What is the state? ").lower()
if state == 'wi' or state == 'wisconsin':
    tax = order_amount * .055
    print(f"The subtotal is {order_amount}")
    print(f"The tax is {tax}")
    total += tax
total = round(total, 2)
print(f"The total is {total}")
