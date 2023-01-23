# import os

# fp = open('ex20.txt', 'r+')
# text = fp.readlines()
# phrase = " IL Sales Tax Rate"
# values = {}
# for line in text:
#     line = line.replace("\t\t", "")
#     line = line.replace("\t", "")
#     line = line.replace("\n", "")
#     line = line.replace("%", "")
#     line = line.replace(phrase, "")
#     line = line.replace(" County", "")
#     line = line.lower()
#     county = line.split(',')[0]
#     percent = float(line.split(',')[1])
#     values[county] = percent
# print(values)

# I modified this exercise so that I could learn better how to grab data from a text file
# This exercise can be redone with other states and using web scraping from the site I pulled from
# The site is https://www.sale-tax.com/

tax_rates = {'adams': 6.5, 'alexander': 6.25, 'bond': 7.25, 'boone': 7.75, 'brown': 7.5, 'bureau': 7.25, 'calhoun': 8.0,
             'carroll': 6.5, 'cass': 8.25, 'champaign': 7.5, 'christian': 7.25, 'clark': 7.25, 'clay': 6.75,
             'clinton': 6.25, 'coles': 7.25, 'cook': 9.0, 'crawford': 6.25, 'cumberland': 7.25, 'de witt': 6.25,
             'dekalb': 6.25, 'douglas': 7.25, 'dupage': 7.0, 'edgar': 8.25, 'edwards': 7.25, 'effingham': 6.5,
             'fayette': 7.25, 'ford': 6.25, 'franklin': 8.25, 'fulton': 7.75, 'gallatin': 7.25, 'greene': 7.25,
             'grundy': 6.25, 'hamilton': 8.25, 'hancock': 6.25, 'hardin': 8.25, 'henderson': 7.25, 'henry': 7.75,
             'iroquois': 6.5, 'jackson': 7.25, 'jasper': 7.25, 'jefferson': 6.75, 'jersey': 8.0, 'jo daviess': 7.25,
             'johnson': 7.75, 'kane': 7.0, 'kankakee': 6.25, 'kendall': 7.25, 'knox': 7.75, 'lake': 7.0, 'lasalle': 6.5,
             'lawrence': 7.25, 'lee': 7.75, 'livingston': 7.25, 'logan': 8.25, 'macon': 7.75, 'macoupin': 7.25,
             'madison': 6.85, 'marion': 7.5, 'marshall': 6.25, 'mason': 7.25, 'massac': 6.25, 'mcdonough': 8.0,
             'mchenry': 7.0, 'mclean': 6.25, 'menard': 8.25, 'mercer': 7.25, 'monroe': 7.5, 'montgomery': 7.25,
             'morgan': 7.25, 'moultrie': 6.75, 'ogle': 6.25, 'peoria': 7.25, 'perry': 7.75, 'piatt': 7.25, 'pike': 7.75,
             'pope': 6.25, 'pulaski': 6.25, 'putnam': 6.25, 'randolph': 7.25, 'richland': 7.75, 'rock island': 7.25,
             'saint clair': 7.35, 'saline': 8.0, 'sangamon': 7.25, 'schuyler': 7.25, 'scott': 7.25, 'shelby': 7.25,
             'stark': 7.5, 'stephenson': 6.75, 'tazewell': 6.75, 'union': 8.5, 'vermilion': 6.5, 'wabash': 7.25,
             'warren': 7.25, 'washington': 6.25, 'wayne': 7.0, 'white': 7.25, 'whiteside': 7.25, 'will': 7.0,
             'williamson': 7.25, 'winnebago': 7.75, 'woodford': 8.25}

# prompt for order amount
order = float(input("What is the cost of your order? "))
# prompt for county and tax accordingly
county = input("What Illinois county are you paying sales tax in? ").lower()
county_rate = tax_rates[county] * .01
# print tax amount, then order amount
tax = order * county_rate
print(f"The sales tax on your order is ${tax}.")
total = round(order + tax, 2)
print(f"Your total is ${total}.")
