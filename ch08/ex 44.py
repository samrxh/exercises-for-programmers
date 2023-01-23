import json
from babel.numbers import format_currency


def search_json():
    f = open('ex44.json', 'r+')
    data = json.load(f)
    count = 0
    item_found = False
    while item_found is False:
        name = input("Product: ").lower()
        for i in data['products']:
            if name in i['name'].lower():
                print(f"Name: {i['name']}")
                print(f"Price: {format_currency(i['price'], 'USD', locale='en_US')}")
                print(f"Quantity on hand: {i['quantity']}")
                count += 1
                item_found = True
        if count == 0:
            print("No product found.")
            # the following is commented out because i can't figure out how to append the new product
            # make_new = input("Add product to list? ")
            # if make_new == 'y':
            #     f.close()
            #     f = open('ex44.json', 'w')
            #     name = input("Type product: ")
            #     price = input("Type price: ")
            #     quantity = input("Type quantity on hand: ")
            #     product = {'name': name, 'price': price, 'quantity': quantity}
            #     json_object = json.dumps(product)
            #     f.write(json_object)
            #     f.close()
    f.close()


search_json()
