import api_key
from flask import Flask, render_template, request, redirect, url_for
import requests


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
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

        # return f'location: {location}, units: {units}, API url: {index.url}'
        return redirect(url_for('analyze_weather')), index.url

    else:
        return render_template("index.html")


@app.route('/attireweather', methods=['POST', 'GET'])
def analyze_weather():
    # API variables
    url = index.url
    response = requests.get(url)
    content_type = response.headers.get('Content-Type')
    request = response.request
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
    
    return render_template('attireweather.html', location=location, units=units, temp=temp, tempF=tempF, temp_feel=temp_feel, rain_chance=rain_chance, precip=precip, turbulence=turbulence, humidity=humidity)

if __name__=='__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')