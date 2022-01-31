import api_key
from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)


# a comprehensive list that appears at the end of the program with what clothing to wear
what_to_wear = []

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        city = request.form.get("city")
        state = request.form.get("state")
        units = request.form.get("units")
        
        # check location for validity, translate state abbreviations to full names
        if state:
            location = (f'{city.strip()},{state.strip()}')
        else:
            location = city.strip()
        
        global url
        url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key.key}'
        
        return f'location: {location}, units: {units}, API url: {url}'

    else:
        return render_template("index.html")


# @app.route('/attire_weather', methods=['POST', 'GET'])
# def analyze_weather(url):
#     # API variables
#     response = requests.get(url)
#     content_type = response.headers.get('Content-Type')
#     request = response.request
#     json_data = response.json()

#     # weather variable queries
#     location = url.split("=")[1].split("&")[0].title().replace(',', ', ')
#     units = url.split("80")[1].split("&units=")[1]
#     temp = json_data['main']['temp']
#     tempF = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location.strip()}&appid={api_key.key}&units=imperial').json()['main']['temp']
#     temp_feel = json_data['main']['feels_like']
#     rain_chance = json_data['clouds']['all']
#     precip = json_data['weather'][0]['main'].lower()
#     turbulence = json_data['wind']['speed']
#     humidity = json_data['main']['humidity']
#     print('~'*80)
#     print(f'The current temperature in {location} is {temp}. It feels like {temp_feel}.')

#     if tempF > 69:
#         print("It's pretty warm. You'll want to wear minimal clothing like shorts and a tank top on your run.\n")
#         what_to_wear.extend(('shorts', 'tank top',))
#     elif tempF > 44:
#         print("Not too hot, not too cold. You can probably wear shorts and a t-shirt on your run, but you might start with a light jacket on top.\n")
#         what_to_wear.extend(('shorts', 't-shirt', 'maybe: jacket',))
#     elif tempF > 29:
#         print("Chilly. You'll want to wear pants, a long sleeved shirt, ear/nose/mouth protection (buff/hat/headband), and gloves. You might supplement this with a jacket.\n")
#         what_to_wear.extend(('pants', 'long-sleeved shirt', 'buff/hat/headband', 'gloves', 'jacket',))
#     elif tempF > 14:
#         print("Brr. Wear warm pants, a jacket/hoodie, a long-sleeved shirt, ear/nose/mouth protection (buff/hat/headband), and gloves.\n")
#         what_to_wear.extend(('pants', 'long-sleeved shirt', 'buff/hat/headband', 'gloves', 'jacket',))
#     else:
#         print("""*shiver* It's pretty cold. If you must run outdoors, wear pants, a thick jacket, ear/nose/mouth protection (buff/hat/headband), and gloves.
#         Make sure none of your skin is exposed around your ankles/wrists/face, or you could get frostbite.\n""")
#         what_to_wear.extend(('pants', 'long-sleeved shirt', 'buff/hat/headband', 'gloves', 'jacket', 'potentially wear extra layers',))

#     print(f'It is {rain_chance}% cloudy')
#     print('It is always wise to wear sunscreen when running outdoors. A ball cap adds another layer of protection.')
#     what_to_wear.extend(('sunscreen',))
#     if rain_chance < 70:
#         print("It's pretty sunny. You might want to wear sunglasses.")
#         what_to_wear.extend(('maybe: sunglasses', 'ballcap'))

#     if precip == "clear":
#         print(f'It appears to be {precip}.')
#     elif precip.endswith('s'):
#         print(f'There appear to be {precip}.')
#     else:
#         print(f'There appears to be {precip}.')

#     if rain_chance > 75:
#         if tempF < 60:
#             print("You might consider a jacket. It's looking stormy and cool.\n")
#             what_to_wear.extend(('maybe: jacket'))

#     if units == "imperial":
#         print(f'The wind is blowing at {turbulence}mph')
#     else:
#         print(f'The wind is blowing at {turbulence}kph')

#     print(f'The humidity is {humidity}%')
#     if humidity > 50:
#         if tempF > 70:
#             print("Drink lots of water today! It's hot and humid!")

#     print('~'*80)
#     print('On your run, you should consider wearing:')
#     for item in what_to_wear:
#         print(item)



if __name__=='__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')