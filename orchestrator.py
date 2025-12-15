from agents.weather_agent import get_weather
from agents.activity_agent import suggest_activity
from agents.food_agent import suggest_food
from agents.location_agent import suggest_location
from agents.outfit_agent import suggest_outfit

def run(city: str, food_preferences: str):
    """
    Пошаговое построение вечернего плана.
    """
    result = {}

    # 1. Погода
    weather_text = get_weather(city)
    result["weather"] = weather_text

    # 2. Вечерние активности
    activities = suggest_activity(weather_text)
    result["activity"] = activities

    # 3. Еда/закуски
    foods = suggest_food(food_preferences)
    result["food"] = foods

    # 4. Локации
    locations = suggest_location(activities, city)
    result["location"] = locations

    # 5. Одежда
    outfit = suggest_outfit(activities, weather_text)
    result["outfit"] = outfit

    return result
