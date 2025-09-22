I built a FastAPI with two endpoints: one fetches GitHub user details, and the other fetches current weather data for a city using OpenWeather.

### Setup
- Install dependencies ```pip install fastapi uvicorn requests python-dotenv```
- Create environment file
Create a .env file in the project root: ```API_KEY=your_openweather_api_key_here```
Get your free API key from OpenWeatherMap
- Run the application ```uvicorn main:app --reload```

### Usage
Once running, the API will be available at http://localhost:8000

### Endpoints
- Get GitHub User Info  GET ```/get_github_user?username=sharanya123-khanderao```
- Returns user profile data including name, public repos, followers, and following count.

- Get Weather Data GET ``` /get_weather/london```
- Returns current weather information including temperature and description.

Output files are displayed as .png in this repo
