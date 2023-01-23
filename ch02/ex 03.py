quote_db = []


def quoter(quo, auth):
    quote_db.append((quo, auth))
    return f"{auth} says, \"{quo}\""


while True:
    quote = input('What is the quote? ')
    author = input('Who said it? ')
    print(quoter(quote, author))
