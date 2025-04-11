from fastapi import FastAPI
from app.routes.routes import router as weather_router
from app.core.database import Base, engine

#Instancia de FastAPI con titulo y versión
app = FastAPI(title="Weather app",version="1.0")

#Incluir rutas de la API
app.include_router(weather_router)

#Crear tablas si no las hay
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "SkyNow Up and running"}

