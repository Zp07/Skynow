from pydantic import BaseModel
from datetime import datetime

#Esquema de respuesta que extiende de su padre
class WeatherResponse(BaseModel):
    #Propiedades geograficas
    id: int
    city: str
    region: str
    country: str
    latitude: float
    longitude: float
    timezone: str

    #Propiedades meteorologicas
    temperature : float
    humidity : int
    condition : str
    wind_speed : float
    wind_direction : str
    pressure : float
    precipitation : float
    cloud_cover : int
    feels_like : float
    dew_point : float
    visibility : float
    uv_index : int
    gust_speed : float
    
    #Propiedad de registro
    recorded_at: datetime
    
    #Configuración de Pydantic
    class Config:
        from_attributes = True