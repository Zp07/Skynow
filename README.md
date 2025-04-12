# 🌤️ Skynow - Weather Data Collector API

Skynow es una API RESTful construida con FastAPI que recolecta datos climáticos de múltiples ciudades del mundo cada 30 minutos. Almacena esta información en una base de datos PostgreSQL y la exporta automáticamente a archivos CSV diariamente. Es el primer paso de un sistema más grande de análisis y predicción meteorológica con inteligencia artificial.

---

## 🚀 Características

- Consulta actual del clima de múltiples ciudades.
- Recolección automática cada 30 minutos usando `schedule.py`.
- Exportación diaria de datos en formato CSV a medianoche (00:00).
- Endpoint manual `/export` para generar el CSV del día actual.
- Preparado para entrenar modelos de IA a futuro con datos históricos.
- Contenedor Docker listo para producción y desarrollo.

---

## 📦 Stack tecnológico

- **Backend**: FastAPI
- **Base de datos**: PostgreSQL
- **ORM**: SQLAlchemy
- **Automatización**: Schedule
- **Cliente HTTP**: Requests
- **Contenedores**: Docker + Docker Compose

---

## 📁 Estructura del proyecto
