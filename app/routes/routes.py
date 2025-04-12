import os
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.schedule import fetch_and_store_weather
from app.core.export_csv import export_csv
from app.models.models import WeatherData
from app.schemas.schemas import WeatherResponse
from app.services.weather_api import get_weather_city

router = APIRouter()

#Obtener datos del clima en tiempo real y almacenarlo en BD 
@router.get("/weather/{city}", response_model=WeatherResponse)
def get_weather_api(city: str, db: Session = Depends(get_db)):
    weather_data = get_weather_city(city)

    if not weather_data:
        raise HTTPException(status_code=404, detail="City not found")
    
    new_entry = WeatherData(**weather_data)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return new_entry

# Consumir API MANUALMENTE del modulo schedule
@router.post("/weather/fetch_all")
def fetch_all_weather():
    "Ejecuta manualmente el modulo schedule"
    try:
        fetch_and_store_weather()
        return {"message": "✅ Recolección manual completada "}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Error: {str(e)}")

#Exportar datos de la BD a un archivo CSV
@router.get("/export")
def export_weather_data():
    filename = export_csv()

    if not filename:
        raise HTTPException(status_code=404, detail="No data to export")
    
    return FileResponse(
        path=filename, 
        filename=os.path.basename(filename), 
        media_type='text/csv')


    
