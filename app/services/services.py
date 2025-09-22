import os
import requests
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
GITHUB_API_URL = "https://api.github.com/users/"
OPENWEATHER_city_URL = "http://api.openweathermap.org/geo/1.0/direct"
OPENWEATHER_coordinates_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_github_user_data(username):
    url = f"{GITHUB_API_URL}{username}"
    try:
        response = requests.get(url)
        if response.status_code == 404:
            raise HTTPException(status_code=404, err_text="GitHub user not found")
        if response.status_code == 403:
            raise HTTPException(status_code=403, err_text="GitHub API rate limit exceeded")
        response.raise_for_status()
        
        user_data = response.json()
        return {
            "login": user_data.get("login"),
            "name": user_data.get("name"),
            "public_repos": user_data.get("public_repos"),
            "followers": user_data.get("followers"),
            "following": user_data.get("following"),
        }
    except requests.exceptions.RequestException as exc:
        raise HTTPException(status_code=500, err_text=f"A network error occurred: {exc}")


def fetch_city_weather_data(city):
    try:
        city_params = {"q": city, "limit": 1, "appid": API_KEY}
        city_response = requests.get(OPENWEATHER_city_URL, params=city_params)
        city_response.raise_for_status()
        location_data = city_response.json()

        if not location_data:
            raise HTTPException(status_code=404, err_text=f"City '{city}' not found.")

        lat, lon = location_data[0]["lat"], location_data[0]["lon"]

        city_coordinates_params = {"lat": lat, "lon": lon, "appid": API_KEY, "units": "metric"}
        weather_response = requests.get(OPENWEATHER_coordinates_URL, params=city_coordinates_params)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        return {
            "city": weather_data.get("name"),
            "temperature": weather_data["main"]["temp"],
            "weather_description": weather_data["weather"][0]["description"],
        }

    except requests.exceptions.RequestException as exc:
        raise HTTPException(status_code=500, err_text=f"A network error occurred: {exc}")
