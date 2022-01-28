import json
import requests
import api_key

url = f"https://api.openweathermap.org/data/2.5/weather?q=Louisville,kentucky&appid={api_key.key}&units=imperial"
response = requests.get(url)
content_type = response.headers.get('Content-Type')
request = response.request

json_data = response.json()

tempF = json_data['main']['temp']
turbulence = json_data['wind']['speed']
rain_or_shine = json_data['clouds']['all']
print(tempF)
print(turbulence)
print(rain_or_shine)

# f = open("weather.json", 'a')
# f.write(f"{response.json()}\n")

