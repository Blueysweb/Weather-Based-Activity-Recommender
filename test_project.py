from project import get_weather_condition, suggest_activity, get_coordinates


def test_get_weather_condition():
    # Test each weather code returns correct condition
    assert get_weather_condition(0) == "Sunny"
    assert get_weather_condition(1) == "Cloudy"
    assert get_weather_condition(2) == "Cloudy"
    assert get_weather_condition(3) == "Cloudy"
    assert get_weather_condition(45) == "Foggy"
    assert get_weather_condition(48) == "Foggy"
    assert get_weather_condition(51) == "Drizzly"
    assert get_weather_condition(61) == "Rainy"
    assert get_weather_condition(71) == "Snowy"
    assert get_weather_condition(80) == "Showery"
    assert get_weather_condition(95) == "Thunderstorm"
    assert get_weather_condition(999) == "Unknown"


def test_suggest_activity():
    # Define the valid activities for each condition
    sunny_activities = [
        "go for a walk",
        "have a picnic",
        "go cycling",
        "visit a park",
        "go swimming"
    ]
    rainy_activities = [
        "watch a movie",
        "read a book",
        "cook a new recipe",
        "do a puzzle",
        "listen to a podcast"
    ]
    cloudy_activities = [
        "visit a museum",
        "go shopping",
        "explore a new café",
        "take photos outside",
        "visit a friend"
    ]
    snowy_activities = [
        "build a snowman",
        "go skiing",
        "have hot chocolate indoors",
        "take a winter walk",
        "watch a cozy movie"
    ]
    thunderstorm_activities = [
        "stay indoors and relax",
        "play board games",
        "do a home workout",
        "organize your room",
        "journal your thoughts"
    ]
    foggy_activities = [
        "meditate at home",
        "do indoor exercise",
        "read a book",
        "cook something warm",
        "catch up with friends online"
    ]
    drizzly_activities = [
        "visit an indoor market",
        "go to a coffee shop",
        "watch a documentary",
        "do some light stretching",
        "write in a journal"
    ]
    showery_activities = [
        "visit a gallery",
        "bake something",
        "do a home spa day",
        "play video games",
        "learn something new online"
    ]

    # Check each condition returns an activity from its correct list
    assert suggest_activity("Sunny") in sunny_activities
    assert suggest_activity("Rainy") in rainy_activities
    assert suggest_activity("Cloudy") in cloudy_activities
    assert suggest_activity("Snowy") in snowy_activities
    assert suggest_activity("Thunderstorm") in thunderstorm_activities
    assert suggest_activity("Foggy") in foggy_activities
    assert suggest_activity("Drizzly") in drizzly_activities
    assert suggest_activity("Showery") in showery_activities

    # Unknown condition should return fallback
    assert suggest_activity("Unknown") == "stay home and relax"
    assert suggest_activity("") == "stay home and relax"


def test_get_coordinates():
    # Test a well-known city returns valid coordinates
    lat, lon = get_coordinates("London")
    assert lat is not None
    assert lon is not None
    assert isinstance(lat, float)
    assert isinstance(lon, float)

    # Test another known city
    lat, lon = get_coordinates("Abuja")
    assert lat is not None
    assert lon is not None

    # Test invalid location returns None, None
    lat, lon = get_coordinates("xyzxyzxyzinvalidcity123")
    assert lat is None
    assert lon is None