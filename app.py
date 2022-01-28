import requests
import api_key


def get_location(location = input("Provide your city,state without a space: ")):

    # use regex to check location

    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key.key}'

    return url

url = get_location()  

def get_units(units_choice = input("Do you prefer to see the weather in imperial or metric units? Type 'imperial' or 'metric': ")):

    global url
    imperial = '&units=imperial'
    metric = '&units=metric'

    if units_choice == "imperial":
        print("We'll show you the weather in imperial units.")
        url += imperial
    elif units_choice == "metric":
        print("We'll show you the weather in metric units.")
        url += metric
    else:
        print("Incorrect input. We'll show you the weather in imperial units.")
        url += imperial

    return url

url = get_units()


response = requests.get(url)
content_type = response.headers.get('Content-Type')
request = response.request
json_data = response.json()

tempF = json_data['main']['temp']
temp_feel = json_data['main']['feels_like']
rain_or_shine = json_data['clouds']['all']
precip = json_data['weather'][0]['main']
turbulence = json_data['wind']['speed']
humidity = json_data['main']['humidity']

print(f'The current temperature is {tempF}F')
print(f'It feels like {temp_feel}F')
print(f'It is {rain_or_shine}% cloudy')
print(f'There appears to be {precip.lower()}')
print(f'The wind is blowing at {turbulence}mph')
print(f'The humidity is {humidity}%')

### running attire app wireframe ###

## welcome user

## allow user to input US zipcode OR city, state and append to URL
## ask user if they prefer metric or imperial - do Americans know what this is? - and append to URL

## target all weather variables that noticeably affect run conditions
    # temp
        # real feel temp
    # sun
    # precipitation
    # wind
    # humidity

## determine what the user needs for each change in weather variable via comparison statements

# temp
    # if it's above 70, wear shorts and tank top
    # if it's above 45, wear shorts and tshirt
    # it it's above 30, wear pants, long sleeved shirt, ear/nose/mouth protection (buff/hat/headband), gloves
    # if it's above 15, wear pants, jacket/hoodie, ear/nose/mouth protection (buff/hat/headband), gloves
    # if it's above 0, wear pants, jacket/hoodie, ear/nose/mouth protection (buff/hat/headband), gloves - or maybe don't go out

# sun
    # remind user to always protect skin from sun - sunscreen, hat
    # if sun is out, wear sunglasses too

# precipitation
    # if raining and temp is below 70, wear rain jacket
    # if snowing and not windy, wear shoes with extra traction
    # if snowing and windy, wear shoes with extra traction AND protect all skin with extra clothes

# wind
    # if windy, alert user they might need to dress warmer than anticipated
    # if windy and precipitating, protect eyes
    # if not windy - looks like an easy day!

# humidity
    # if above 50% humidity and above 70, remind user to drink extra water
    # if 50% humidity or below, looks like a nice, dry day

# use Flask and turn all of this into a web app!