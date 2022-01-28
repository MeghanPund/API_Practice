import requests
import api_key

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Louisville,kentucky&appid={api_key.key}&units=imperial")
request = response.request


f = open("weather.json", 'a')
f.write(f"{response.text}\n")

