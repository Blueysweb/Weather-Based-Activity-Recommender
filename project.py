from geopy.geocoders import Nominatim
import random
import requests


def main():
    name = input("Welcome to my weather app! please enter your name: ")
    location = input("What is your location? ")
    lat, lon = get_coordinates(location)
    code = get_weather(lat, lon)
    condition = get_weather_condition(code)
    activity = suggest_activity(condition)
    print(f"\nHello, {name}!")
    print(f"The weather in {location} is {condition}")
    print(f"You should {activity}")
    
def get_coordinates(location):
    locator = Nominatim(user_agent="my_weather_app")
    location_info = locator.geocode(location)
    if location_info:
        return location_info.latitude, location_info.longitude
    else:
        print("Location not found.")
        return None, None


def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    return data["current_weather"]["weathercode"]


def get_weather_condition(code):
    if code == 0:
        return "Sunny"
    elif code in [1, 2, 3]:
        return "Cloudy"
    elif code in [45, 48]:
        return "Foggy"
    elif code in [51, 53, 55]:
        return "Drizzly"
    elif code in [61, 63, 65]:
        return "Rainy"
    elif code in [71, 73, 75]:
        return "Snowy"
    elif code in [80, 81, 82]:
        return "Showery"
    elif code in [95, 96, 99]:
        return "Thunderstorm"
    else:
        return "Unknown"


def suggest_activity(condition):
    activities = {
       "Sunny": [
            "go for a walk",
            "have a picnic",
            "go cycling",
            "visit a park",
            "go swimming"
        ],
         "Rainy": [
            "watch a movie",
            "read a book",
            "cook a new recipe",
            "do a puzzle",
            "listen to a podcast"
         ],
          "Cloudy": [
            "visit a museum",
            "go shopping",
            "explore a new café",
            "take photos outside",
            "visit a friend"
        ],
          "Snowy": [
            "build a snowman",
            "go skiing",
            "have hot chocolate indoors",
            "take a winter walk",
            "watch a cozy movie"
        ],
            "Thunderstorm": [
            "stay indoors and relax",
            "play board games",
            "do a home workout",
            "organize your room",
            "journal your thoughts"
        ],
             "Foggy": [
            "meditate at home",
            "do indoor exercise",
            "read a book",
            "cook something warm",
            "catch up with friends online"
        ],
        "Drizzly": [
            "visit an indoor market",
            "go to a coffee shop",
            "watch a documentary",
            "do some light stretching",
            "write in a journal"
        ],
        "Showery": [
            "visit a gallery",
            "bake something",
            "do a home spa day",
            "play video games",
            "learn something new online"
        ]
    }
    
    if condition in activities:
        return random.choice(activities[condition])
    else:
        return "stay home and relax"




if __name__ == "__main__":
    main()