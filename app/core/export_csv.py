import pandas as pd
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.models import WeatherData
from datetime import datetime
import os


def export_csv():
    db: Session = SessionLocal()

    # Se obtienen los datos de la base de datos
    weather_records = db.query(WeatherData).all()
    db.close()

    if not weather_records:
        print("No hay datos para exportar")
        return
    
    # Crear el directorio de exportación si no existe
    os.makedirs("exports", exist_ok=True)
    
    # Convertir los datos a un DataFrame
    data = [{
        "id": record.id,
        "city": record.city,
        "region": record.region,
        "country": record.country,
        "latitude": record.latitude,
        "longitude": record.longitude,
        "timezone": record.timezone,
        "temperature": record.temperature,
        "humidity": record.humidity,
        "condition": record.condition,
        "wind_speed": record.wind_speed,
        "wind_direction": record.wind_direction,
        "pressure": record.pressure,
        "precipitation": record.precitipation,
        "cloud_cover": record.cloud_cover,
        "feels_like": record.feels_like,
        "dew_point": record.dew_point,
        "visibility": record.visibility,
        "uv_index": record.uv_index,
    
        "gust_speed": record.gust_speed,
        "recorded_at": record.recorded_at.strftime("%Y-%m-%d %H:%M:%S"),
        "created_at": record.created_at.strftime("%Y-%m-%d %H:%M:%S"),
    } 
    for record in weather_records ]

    # Crear un DataFrame
    df = pd.DataFrame(data)

    # Definir el nombre del archivo con la fecha
    filename = f"exports/weather_data_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"

    # Guardar en CSV
    df.to_csv(filename, index=False)
    print(f"Archivo CSV exportado: {filename}")
    return filename
