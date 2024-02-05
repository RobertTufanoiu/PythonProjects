import datetime as dt 
import requests 

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "512bfff06003382f3012aa3a016e9add"
CITY = "Bucharest"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY 

response = requests.get(url).json()

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius 

temp_kelvin = response['main']['temp']
temp_celsius = kelvin_to_celsius(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'])
wind_speed = response['wind']['speed']

print(f"Temperature in {CITY} is {temp_celsius:.2f} degrees Celsius")
print(f"Temperature in {CITY} feels like {feels_like_celsius:.2f} degrees Celsius")
print(f"Humidity in {CITY} is {humidity}%")
print(f"Windspeed in {CITY} is {wind_speed} meters per second")
print(f"General weather in {CITY}: {description}")
print(f"The sun rises in {CITY} at {sunrise_time} local time")
print(f"The sun sets in {CITY} at {sunset_time} local time")






