import pandas as pd
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.models import WeatherData
from datetime import datetime

def export_csv():
    db: Session = SessionLocal()

    # Se obtienen los datos de la base de datos
    weather_records = db.query(WeatherData).all()
    db.close()

    if not weather_records:
        print("No hay datos para exportar")
        return
    
    # Convertir los datos a un DataFrame
    data = [{
        "id": record.id,
        "city": record.city,
        "temperature": record.temperature,
        "humidity": record.humidity,
        "condition": record.condition,
        "wind_speed": record.wind_speed,
        "wind_direction": record.wind_direction,
        "pressure": record.pressure,
        "precipitation": record.precipitation,
        "recorded_at": record.recorded_at.strftime("%Y-%m-%d %H:%M:%S")
    } 
    for record in weather_records ]

    # Crear un DataFrame
    df = pd.DataFrame(data)

    # Definir el nombre del archivo con la fecha
    filename = f"weather_data_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"

    # Guardar en CSV
    df.to_csv(f"exports/{filename}", index=False)
    print(f"Archivo CSV exportado: {filename}")

if __name__ == "__main__":
    export_csv()
