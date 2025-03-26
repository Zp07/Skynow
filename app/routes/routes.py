from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
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

#
    
