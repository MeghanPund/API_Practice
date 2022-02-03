# Running Attire App
## Program Description
Acquires user’s location, calls Open Weather Map API, analyzes the weather at user’s location,
and returns suggested running clothes based on the weather conditions.

## A Link to the Application, hosted on GCP with App Engine
[(https://runningattireflaskapp.uc.r.appspot.com/)]

## Functionality
1. Accepts user input for location and desired units (imperial or metric).
2. Calls Open Weather Map API with user's location input and queries for the temperature, real feel temperature,
wind speed, chance of precipitation, kind of precipitation, humidity, etc.
3. Through a series of if/else comparisions in Python, determines appropriate clothing
based on the weather at that location.
4. Displays the weather conditions and suggested clothing back to the user.
5. Displays a running-relevant quote randomly selected from a list of quotes.

## Improvements to be made
1. Better CSS/styling and organization/layout.
2. Accept and translate state abbreviations to input the API can process (many users are inclined
 to enter KY instead of Kentucky)
3. Add appropriate weather icons (clouds, sun, snowflake) and other experience-enhancing 
material to the attire suggestions page.

