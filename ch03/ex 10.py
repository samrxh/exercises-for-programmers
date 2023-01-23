def item_info(item_number):
    for i in range(item_number):
        item_price = int(input(f"Enter the price of item {i+1}: "))
        item_quant = int(input(f"Enter the quantity of item {i+1}: "))
        yield item_price, item_quant


subtotal = 0
for item in item_info(int(input("How many items? "))):
    price = item[0] * item[1]
    subtotal += price
subtotal = round(subtotal, 2)
tax = round(subtotal * .055, 2)
total = round(subtotal + tax, 2)
# Issue below with the .x0 price point. Solutions involve importing a package.
print(f"Subtotal: ${subtotal}")
print(f"Tax: ${tax}")
print(f"Total: ${total}")
