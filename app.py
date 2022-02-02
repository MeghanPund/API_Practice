from distutils.log import error
import api_key
from flask import Flask, render_template, request, redirect, url_for
import random
import requests


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    error = None
    if request.method == 'POST':
        if not request.form.get("city"):
            error = "You need to enter a city name."
        else:
            city = request.form.get("city")
            state = request.form.get("state")
            units = request.form.get("units")
            imperial = '&units=imperial'
            metric = '&units=metric'

            # check location for validity, translate state abbreviations to full names
            if state:
                location = (f'{city.strip()},{state.strip()}')
            else:
                location = city.strip()
            
            index.url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key.key}'
            
            if units == 'metric':
                index.url += metric
            else:
                index.url += imperial

            return redirect(url_for('analyze_weather'))
        
        return render_template("index.html", error=error)
    else:
        return render_template("index.html")


@app.route('/attireweather', methods=['POST', 'GET'])
def analyze_weather():
    # API variables
    url = index.url
    response = requests.get(url)
    json_data = response.json()

    # weather variable queries
    location = url.split("=")[1].split("&")[0].title().replace(',', ', ')
    units = url.split("80")[1].split("&units=")[1]
    temp = json_data['main']['temp']
    tempF = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location.strip()}&appid={api_key.key}&units=imperial').json()['main']['temp']
    temp_feel = json_data['main']['feels_like']
    rain_chance = json_data['clouds']['all']
    precip = json_data['weather'][0]['main'].lower()
    turbulence = json_data['wind']['speed']
    humidity = json_data['main']['humidity']

    quotes = ['“I don\'t run to add days to my life, I run to add life to my days.” — Ronald Rook',
    '“Running is the greatest metaphor for life, because you get out of it what you put into it.” — Oprah Winfrey',
    '“We are what we repeatedly do. Excellence, then, is not an act, but a habit.” — Aristotle',
    '“If it doesn\'t challenge you, it won\'t change you.” — Fred DeVito',
    '“The man who moves a mountain begins by carrying away small stones.” — Confucius',
    '“Someone who is busier than you is running right now.” — Nike',
    '"Only those who risk going too far can possibly find out how far one can go." — T. S. Eliot.',
    ]
    quote = random.choice(quotes)
    
    return render_template('attireweather.html', quote=quote, location=location, units=units, temp=temp, tempF=tempF, temp_feel=temp_feel, rain_chance=rain_chance, precip=precip, turbulence=turbulence, humidity=humidity)

if __name__=='__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')