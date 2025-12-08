import httpx
import os


OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")


async def get_weather_by_city(city: str, units: str = "metric") -> dict:
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
"q": city,
"appid": OPENWEATHER_KEY,
"units": units,
"lang": "ru"
}
async with httpx.AsyncClient() as client:
r = await client.get(url, params=params, timeout=10)
r.raise_for_status()
return r.json()