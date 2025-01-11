import requests
import os

parameters = {
    'lat':19.997454,
    'lon':73.789803,
    'appid':'2e76ce2e4b1cb1cfa7a4f56aff949ad6',
}
response = requests.get(url='https://api.openweathermap.org/data/2.5/weather',params=parameters)
response.raise_for_status()
data = response.json()['weather'][0]['id']
if data <600:
    print("Bring an umbrella! it might rain today")
else:
    print("No need to bring an umbrella")
