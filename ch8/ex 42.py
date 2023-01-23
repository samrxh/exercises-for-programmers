from babel.numbers import format_currency

with open('ex42.txt', 'r+') as file:
    lines = [line.strip().split(',') for line in file]
    people = []
    for line in lines:
        last = line[0]
        first = line[1]
        salary = format_currency(line[2], 'USD', locale='en_US')
        person = {'last': last, 'first': first, 'salary': salary}
        people.append(person)
    print("Last\t\t\tFirst\t\tSalary")
    people = sorted(people, key=lambda x: x['salary'])
    for item in people:
        print(f"{item['last']}\t\t\t{item['first']}\t\t\t{item['salary']}")

    # the proper spacing can be achieved with the below method, but it would require
    # each person to be stored as a list instead of a dictionary. maybe that's better...
    #
    # for item in people:
    #     for key, value in item.items():
    #         last, first, salary = value
    #         print("{:<10} {:<10} {:<10}".format(last, first, salary))