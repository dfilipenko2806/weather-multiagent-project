from services.weather_api import get_weather

def get_summary(city: str):
    data = get_weather(city)

    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]

    return f"Температура {temp}°C, {description}"
