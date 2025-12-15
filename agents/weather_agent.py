import requests
from config import OPENWEATHER_API_KEY

def get_weather(city: str) -> str:
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return f"N/A°C, No description"

        temp = data['main']['temp']
        description = data['weather'][0]['description']

        return f"{temp}°C, {description}"

    except Exception as e:
        return f"N/A°C, No description"
