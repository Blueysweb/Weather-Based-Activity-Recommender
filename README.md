# Weather-Based Activity Recommender

#### Video Demo: <URL https://www.youtube.com/watch?v=XO6mQc0R8T0 >

#### Description:

## What is this project?

Weather-Based Activity Recommender is a Python command-line program that
takes a user's name and location as input, fetches the current weather
for that location, and recommends a random activity suited to the
current weather conditions. The goal is to help users decide what to do
with their day based on real-time weather data, in a simple, friendly,
and interactive way.

This project was built as the final project for CS50's Introduction to
Programming with Python (CS50P).

---

## How it works

When the user runs the program, they are greeted and prompted to enter
their name and their current location (city or country). The program
then:

1. Converts the location into geographic coordinates (latitude and
longitude) using the Nominatim geocoding service from the geopy library.
2. Sends those coordinates to the Open-Meteo API, a free and open-source
weather API that requires no API key, to fetch the current weather code
for that location.
3. Converts the numeric weather code into a human-readable weather
condition such as "Sunny", "Rainy", "Cloudy", "Snowy", "Foggy",
"Drizzly", "Showery", or "Thunderstorm".
4. Randomly selects one activity from a curated list of five activities
suited to that weather condition.
5. Displays a personalized greeting along with the current weather
condition and the recommended activity.

---

## Files in this project

### `project.py`

This is the main program file. It contains the following functions:

- **`main()`** — The entry point of the program. Handles user input,
calls all other functions in sequence, and displays the final output
to the user. It also handles the case where a location cannot be found,
printing a friendly error message and exiting gracefully.

- **`get_coordinates(location)`** — Takes a location string (e.g.
"Abuja" or "London") and uses the Nominatim geocoding service to
convert it into a latitude and longitude pair. Returns `(None, None)`
if the location cannot be found, which allows the program to handle
invalid locations without crashing.

- **`get_weather(lat, lon)`** — Takes a latitude and longitude and
makes a request to the Open-Meteo API to fetch the current weather
data. Returns the numeric weather code for the current conditions at
that location. This function uses the `requests` library to make the
HTTP request and parses the JSON response.

- **`get_weather_condition(code)`** — Takes a numeric weather code
returned by Open-Meteo and converts it into a human-readable string
such as "Sunny", "Rainy", or "Thunderstorm". The mapping is based on
the official Open-Meteo weather code documentation. Returns "Unknown"
for any code not covered by the mapping.

- **`suggest_activity(condition)`** — Takes a weather condition string
and returns one randomly selected activity from a curated list of five
activities for that condition. Each weather condition has its own list
of five suitable activities. If the condition is not recognized, the
function returns a safe fallback: "stay home and relax". The random
selection is handled using Python's built-in `random.choice()` function.

### `test_project.py`

This file contains the pytest tests for the project. It tests three of
the custom functions:

- **`test_get_weather_condition()`** — Tests that each weather code
returns the correct condition label. Covers all eight weather conditions
as well as an unknown code.

- **`test_suggest_activity()`** — Tests that each weather condition
returns a valid activity from its expected list. Also tests that an
unknown condition returns the fallback response.

- **`test_get_coordinates()`** — Tests that known cities like London
and Abuja return valid float coordinates, and that an invalid location
returns `(None, None)`.

### `requirements.txt`

Lists the two third-party libraries required to run this project:

- `requests` — used to make HTTP requests to the Open-Meteo weather API
- `geopy` — used to convert location names into geographic coordinates

### `README.md`

This file. Documents the project, its structure, design decisions, and
how to run it.


## How to run the project

1. Clone or download the project files into a folder.
2. Install the required libraries:
