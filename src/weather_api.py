import os
import requests

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        raise Exception("WEATHER_API_KEY not set in environment variables.")
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={api_key}&units=metric"
    )
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()