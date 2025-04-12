import schedule
import time
import traceback
from datetime import datetime
from app.services.weather_api import get_weather_city
from app.core.database import SessionLocal
from app.models.models import WeatherData
from app.config.info import ALL_CITIES
from app.core.export_csv import export_csv

# Configuración de la API
FETCH_INTERVAL = 30 # minutos
CSV_EXPORT_TIME = "23:59" # hora de exportación a CSV
EXPORT_PATH = "exports/weather_data_{today_str}.csv" # ruta de exportación

# Funcion para obtener datos cada 30 min
def fetch_and_store_weather():
    print(f"[{datetime.now()}] ⏳ Iniciando recolección de clima...")
    db = SessionLocal()
    try:
        for city in ALL_CITIES:
            print(f"🌍 Recolectando clima para {city}...")
            # Se obtienen los datos de la API
            weather_data = get_weather_city(city)
            # Se verifica si se obtuvieron datos
            if weather_data:
                new_entry = WeatherData(**weather_data)
                db.add(new_entry)
                print(f"[{datetime.now()}] ✅ Datos guardados para: {city}")
            else:
                print(f"[{datetime.now()}] ⚠️ No se pudieron obtener datos para: {city}")
        
        db.commit()
        print(f"[{datetime.now()}] 💾 Todos los datos fueron guardados.")

    except Exception as e:
        print(f"[{datetime.now()}] ❌ Error en fetch_and_store_weather: {str(e)}")
        traceback.print_exc()

    finally:
        db.close()
        print(f"[{datetime.now()}] 🔒 Sesión cerrada.\n")

# Funcion para exportar datos a CSV automaticos
def export_daily_csv():
    today_str = datetime.now().strftime("%Y-%m-%d")
    filename = EXPORT_PATH.format(date=today_str)
    
    try:
        export_csv(filename=filename)
        print(f"[{datetime.now()}] 📊 Exportación a CSV completada: {filename}")
    
    except Exception as e:
        print(f"[{datetime.now()}] ❌ Error al exportar a CSV: {e}")
        traceback.print_exc()


        
# Se ejecuta la tarea cada 30 minutes
schedule.every(FETCH_INTERVAL).minutes.do(fetch_and_store_weather)

# Se ejecuta la tarea cada dia a las 23:59
schedule.every().day.at(CSV_EXPORT_TIME).do(export_daily_csv)

if __name__ == "__main__":
    print(f"[{datetime.now()}] 🔄 Scheduler iniciado !! 🍄\n")
    # Se ejecuta indefinidamente
    while True:
        schedule.run_pending()
        time.sleep(60)