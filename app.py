import requests
import api_key

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Louisville,kentucky&appid={api_key.key}")
request = response.request

f = open("weather.json", 'a')
f.write(response.text)