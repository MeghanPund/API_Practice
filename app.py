import requests
import api_key


def get_location(location = input("Welcome to the Running Attire App.\nProvide your city,state: ")):

    # check location for validity
    location.replace(" ", "")
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

# API variables
response = requests.get(url)
content_type = response.headers.get('Content-Type')
request = response.request
json_data = response.json()

# weather variable queries
location = url.split("=")[1].split("&")[0].title()
tempF = json_data['main']['temp']
temp_feel = json_data['main']['feels_like']
rain_or_shine = json_data['clouds']['all']
precip = json_data['weather'][0]['main'].lower()
turbulence = json_data['wind']['speed']
humidity = json_data['main']['humidity']

print('')
print(f'The current temperature in {location} is {tempF}F.')
print(f'It feels like {temp_feel}F.')

if tempF > 69:
    print("It's pretty warm. You'll want to wear minimal clothing like shorts and a tank top on your run.\n")
elif tempF > 44:
    print("Not too hot, not too cold. You can probably wear shorts and a t-shirt on your run, but you might start with a light jacket on top.\n")
elif tempF > 29:
    print("Chilly. You'll want to wear pants, a long sleeved shirt, ear/nose/mouth protection (buff/hat/headband), and gloves. You might supplement this with a jacket.\n")
elif tempF > 14:
    print("Brr. Wear warm pants, a jacket/hoodie, ear/nose/mouth protection (buff/hat/headband), and gloves.\n")
else:
    print("""*shiver* It's pretty cold. If you must run outdoors, wear pants, a thicker jacket/hoodie, ear/nose/mouth protection (buff/hat/headband), and gloves.
    Make sure none of your skin is exposed around your ankles/wrists/face, or you could get frostbite.\n""")

print(f'It is {rain_or_shine}% cloudy')
print('It is always wise to wear sunscreen when running outdoors. A ball cap adds another layer of protection.')
if rain_or_shine < 50:
    print("It's pretty sunny. You might want to wear sunglasses.")

if precip.endswith('s'):
    print(f'There appear to be {precip}.')
else:
    print(f'There appears to be {precip}.')
if rain_or_shine > 75:
    if tempF < 60:
        print("You might consider a jacket. It's looking stormy and cool.\n")


print(f'The wind is blowing at {turbulence}mph')
print(f'The humidity is {humidity}%')
if humidity > 50:
    if tempF > 70:
        print("Drink lots of water today! It's hot and humid!")


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