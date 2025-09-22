from fastapi import FastAPI, Query
from services.services import fetch_github_user_data, fetch_city_weather_data

app = FastAPI(title="API Service")


@app.get("/get_github_user")
def get_github_user(username: str = Query(..., description="GitHub username")):
    return fetch_github_user_data(username)


@app.get("/get_weather/{city}")
def get_weather(city: str):
    return fetch_city_weather_data(city)