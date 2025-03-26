import schedule
import time
from app.services.weather_api import get_weather_city
from app.core.database import SessionLocal
from app.models.models import WeatherData
from app.config.info import TOTAL_CITIES

# Funcion para obtener datos cada 2 horas
def fetch_and_store_weather():
    db = SessionLocal()
    for city in TOTAL_CITIES:
        weather_data = get_weather_city(city)
        if weather_data:
            new_entry = WeatherData(**weather_data)
            db.add(new_entry)
    db.commit()
    db.close()

# Se ejecuta la tarea cada 2 horas
schedule.every(2).hours.do(fetch_and_store_weather)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)