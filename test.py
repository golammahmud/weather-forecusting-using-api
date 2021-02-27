import requests
import json
import time
city_name =input('Enter your city:')
api_key = "d20f1fcf3aa34fd2a1ef6c9d168aaf2a"

URL = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

json_data = requests.get(url=URL).json()
condition = json_data['weather'][0]['main']
description=json_data['weather'][0]['description']
temp=int(json_data['main']['temp']-274.15)
feels=int(json_data['main']['feels_like']-274.15)
max_temp=int(json_data['main']['temp_max']-274.15)
min_temp=int(json_data['main']['temp_min']-274.15)
humidity=json_data['main']['humidity']
wind=json_data['wind']['speed']
country=json_data['sys']['country']
city=json_data['name']
sunrise=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']-21600))
sunset=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']-21600))


print(country,city)
print(condition)
print(description)
print(f'temprature:{temp}°C')
print(f'feels like:{feels}°C')
print(f'max temprature is:{max_temp}°C')
print(f'min temprature is:{min_temp}°C')
print(f'humidity:{humidity}%')
print(f'Air speed:{wind} m/s')

print(sunrise)
print(sunset)


