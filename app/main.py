from fastapi import FastAPI, Query
from app.github_service import fetch_github_user_data
from app.weather_service import fetch_city_weather_data


app = FastAPI()

@app.get("/get_github_user")
def get_github_user(username: str = Query(...)):
    return fetch_github_user_data(username)

@app.get("/get_weather/{city}")
def get_weather(city: str):
    return fetch_city_weather_data(city)
