# this ex requires first a call to geocode the entered city or zip, then using coords to get current weather
# I would rather just have the coords set to make the api call once so I hardcoded it into the keychain

from ex48_keychain import appid, lat, lon
import requests
import json
from datetime import datetime


# this line lets me practice on the data sample ahead of time before I call the api for real
# data = json.load(open('ex48.json', 'r'))
# here we can get api data, which is the same as the json.load data we practiced on ahead of time
def get_data():
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}'
    res = requests.get(url, headers={'Accept': 'application/json'})
    if res.status_code == 200:
        api_data = res.json()
        return api_data
    else:
        print(res.status_code)


def compass(num):
    val = int((num / 22.5) + .5)
    arr = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    return arr[(val % 16)]


data = get_data()
temp_k = data['main']['temp']
temp_f = round((temp_k - 273.15) * 1.8 + 32, 2)
temp_c = round(temp_k - 273, 2)
humidity = data['main']['humidity']
weather = data['weather'][0]['description']
sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M')
sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M')
wind_direction = compass(data['wind']['deg'])
wind_speed = round((data['wind']['speed']) / 1609.344, 2)
print(f"""The current temperature is {temp_f}° F / {temp_c}° C.
The current weather: {weather}.
The humidity is {humidity}%.
Sunrise today: {sunrise}.
Sunset today: {sunset}.
Wind: {wind_speed} miles per hour {wind_direction}""")
