import requests
from collections import defaultdict
from nameparser import HumanName


def get_data():
    url = 'http://api.open-notify.org/astros.json'
    res = requests.get(url, headers={'Accept': 'application/json'})
    if res.status_code == 200:
        api_data = res.json()
        return api_data
    else:
        print(res.status_code)


def get_astros(api_data):
    astronauts = [(astronaut['craft'], astronaut['name']) for astronaut in api_data['people']]
    d = defaultdict(list)
    for k, v in astronauts:
        d[k].append(v)
    return d


data = get_data()
print(f"There are {data['number']} people in space right now.\n")
astros = get_astros(data)
for craft in astros.items():
    print(f"People on the {craft[0]}:")
    names = []
    for person in craft[1]:
        name = HumanName(person)
        names.append((name.first, name.last))
    sorted_list = sorted(names, key=lambda x: x[-1])
    for i in sorted_list:
        print(' '.join(i))
    print()

# next up is making this a function, as well as sorting the astronauts by last name in an efficient way
# what can be done about people with spaces in their names?
