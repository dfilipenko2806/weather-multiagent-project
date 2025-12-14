from agents.weather_agent import get_summary
from agents.activity_agent import suggest as activity_suggest
from agents.food_agent import suggest as food_suggest
from agents.location_agent import suggest as location_suggest
from agents.outfit_agent import suggest as outfit_suggest

def run(city, preferences):
    weather = get_summary(city)

    activity = activity_suggest(weather)
    food = food_suggest(activity, preferences)
    location = location_suggest(city, activity)
    outfit = outfit_suggest(weather, activity)

    return {
        "weather": weather,
        "activity": activity,
        "food": food,
        "location": location,
        "outfit": outfit
    }
