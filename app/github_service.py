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
