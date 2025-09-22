import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

GITHUB_API_URL = "https://api.github.com/users/"
OPENWEATHER_city_URL = "http://api.openweathermap.org/geo/1.0/direct"
OPENWEATHER_coordinates_URL = "https://api.openweathermap.org/data/2.5/weather"