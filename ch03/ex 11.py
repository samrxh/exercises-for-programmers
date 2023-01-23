rates = {'usd': 1, 'eur': 1.00228, 'gbp': 1.15771, 'cad': 0.759685, 'aud': 0.681234}  # usd as the base


def convert(rate_from, rate_to, amount):
    return round((amount * rates[rate_from]) / rates[rate_to], 2)


currency_input = input("What currency are you converting from? ")
currency_output = input("What currency are you converting to? ")
amount_convert = int(input("How much are you converting? "))
print(convert(currency_input, currency_output, amount_convert))
