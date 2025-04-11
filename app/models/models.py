from sqlalchemy import Column,Integer,String,Float,DateTime
from app.core.database import Base
from datetime import datetime

#Modelo de la base de datos para almecenar datos meteorológicos
class WeatherData(Base):
    #Nombre de la base de datos
    __tablename__ = "weather_app"

    #Propiedades de la ubicación
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    region = Column(String)
    country = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    timezone = Column(String)

    #Propiedades del clima
    temperature = Column(Float)
    humidity = Column(Integer)
    condition = Column(String)
    wind_speed = Column(Float)
    wind_direction = Column(String)
    pressure = Column(Float)
    precipitation = Column(Float)
    cloud_cover = Column(Integer)
    feels_like = Column(Float)
    dew_point = Column(Float)
    visibility = Column(Float)
    uv_index = Column(Integer)
    gust_speed = Column(Float)

    #Propiedad de fecha de registro
    recorded_at = Column(DateTime, default=datetime.utcnow)