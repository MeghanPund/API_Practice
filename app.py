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

### running attire app wireframe ###

## allow user to input US zipcode OR city, state and append to URL

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