# convert 1-12 to corresponding month, use a dictionary. support multiple languages
number = list(range(1, 13))
month_en = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_es = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
month_it = ['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre']

# zip numbers to months in dictionary. could do this then hardcode? more work dunno
english = dict(zip(number, month_en))
spanish = dict(zip(number, month_es))
italian = dict(zip(number, month_it))

# stackoverflow says not to use eval() w/o restricting user, so I will do that
# of course, you could have a separate path where the program switches to another language. meh
lang = input("What language should we use? ").lower()
if lang in ['english', 'spanish', 'italian']:
    lang = eval(lang)
else:
    print(f"{lang.capitalize()} not in languages.")
    exit()  # I'm being lazy here. :)
month = int(input("What number of month do we want? "))
print(f"The name of the month is {lang[month]}.")
