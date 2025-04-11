import os
import requests

WEATHER_API_KEY= os.getenv("WEATHER_API_KEY")
BASE_URL = os.getenv("WEATHER_API_BASE_URL")

def get_weather_city(city: str):
    
    if not WEATHER_API_KEY:
        raise ValueError("API KEY NOT CONFIG")
    
    params = {
        "key": WEATHER_API_KEY,
        "q": city,
        "aqi": "no"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["location"]["name"],
            "region": data["location"]["region"],
            "country": data["location"]["country"],
            "latitude": data["location"]["lat"],
            "longitude": data["location"]["lon"],
            "timezone": data["location"]["tz_id"],

            "temperature": data["current"]["temp_c"],
            "humidity": data["current"]["humidity"],
            "condition": data["current"]["condition"]["text"],
            "wind_speed": data["current"]["wind_kph"],
            "wind_direction": data["current"]["wind_dir"],
            "pressure": data["current"]["pressure_mb"],
            "precipitation": data["current"]["precip_mm"],
            "cloud_cover": data["current"]["cloud"],
            "feels_like": data["current"]["feelslike_c"],
            "dew_point": data["current"]["dewpoint_c"],
            "visibility": data["current"]["vis_km"],
            "uv_index": data["current"]["uv"],
            "gust_speed": data["current"]["gust_kph"],
        }
    return None