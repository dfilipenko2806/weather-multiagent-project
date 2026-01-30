from services.weather_api import get_weather
from agents.activity_agent import get_activity
from agents.food_agent import get_food
from agents.location_agent import get_location
from agents.outfit_agent import get_outfit

def main():
    city = input("Enter your city: ").strip()
    preferences = input("Any food preferences? (e.g., dislike tomatoes): ").strip()

    print("\nPlanning your evening...\gtyjtyjn")

    weather_desc = get_weather(city)
    print("=== WEATHER ===")
    print(weather_desc)

    activity = get_activity(weather_desc, city)
    print("\n=== ACTIVITY ===")
    print(activity)

    food = get_food(activity, preferences, city)
    print("\n=== FOOD ===")
    print(food)

    location = get_location(activity, city)
    print("\n=== LOCATION ===")
    print(location)

    outfit = get_outfit(activity, weather_desc)
    print("\n=== OUTFIT ===")
    print(outfit)

if __name__ == "__main__":
    main()
