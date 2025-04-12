# 🌤️ SkyNow - API Climática con FastAPI

Skynow es una API RESTful desarrollada en Python utilizando FastAPI, diseñada para recolectar, almacenar y exportar datos meteorológicos de múltiples ciudades. Este proyecto sirve como base para entrenar modelos de inteligencia artificial enfocados en la predicción del clima, abordando problemas reales relacionados con el entorno climático.

---

## 🌍 Misión del Proyecto

Brindar un sistema automatizado, modular y sostenible de recolección de datos climáticos en tiempo real (cada 30 minutos), para alimentar sistemas de análisis e inteligencia artificial. SkyNow apunta a contribuir en áreas como:

- Prevención de daños agrícolas
- Planificación de salidas o eventos
- Monitoreo del clima para turismo
- Gestión ambiental y urbana

---

## 🧱 Arquitectura y Estructura del Proyecto

```
Skynow/
│
├── app/
│   ├── config/           # Configuración global
│   │   └── info.py
│   │
│   ├── core/             # Lógica de negocio principal
│   │   │
│   │   ├- database.py    # Conexión y operaciones con db
│   │   ├── export_csv.py
│   │   └── schedule.py
│   │
│   ├── models/           # Modelos ORM con SQLAlchemy
│   │   └── models.py
│   │
│   ├── routes/           # Endpoints de la API
│   │   └── routes.py
│   │
│   ├── schemas/          # Validación y serialización
│   │   └── schemas.py
│   │
│   └── services/         # Lógica de integración con APIs
│       └── weather_api.py
│
├── main.py               # Punto de entrada de la API
├── Dockerfile            # Imagen Docker del proyecto
├── docker-compose.yml    # Orquestación de servicios
├── .env                  # Variables de entorno
├── .gitignore
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Documentación del proyecto
```

---

## ⚙️ Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y asíncrono
- **PostgreSQL**: Base de datos relacional para almacenamiento histórico
- **SQLAlchemy**: ORM para operaciones con la base de datos
- **Pydantic**: Validación de datos
- **schedule**: Tareas automáticas recurrentes
- **Docker + Docker Compose**: Contenerización y despliegue
- **requests + pandas**: Recolección y manipulación de datos

---

## 🔁 Flujo de Funcionamiento

1. Cada 30 minutos, `schedule.py` ejecuta una solicitud a la API climática y guarda la información en la base de datos.
2. A las 23:59 p.m., `export_csv.py` genera un respaldo en formato `.csv` con los datos del día.
3. La base de datos no borra registros, almacenando un histórico completo.
4. Hay un endpoint `/export` para generar manualmente el archivo CSV del día.
5. Estos datos son usados posteriormente para entrenar modelos de IA en TensorFlow.
6. Se puede forzar manualmente la recolección con /weather/fetch_all
7. Cada petición a /weather/{city} también guarda el dato en la base de datos en tiempo real.

---

## 🧪 Modularidad y Escalabilidad

El proyecto está dividido en módulos bien definidos, lo que permite:

- Mantenimiento sencillo y pruebas unitarias efectivas
- Escalabilidad hacia microservicios
- Incorporación de nuevas fuentes de datos meteorológicos
- Integración de IA sin afectar la arquitectura base

---

## 🧩 Problemas Enfrentados y Decisiones Clave

- Conflictos de `merge` entre ramas `main` y `develop` solucionados con `git reset --hard` y `push --force`
- Se eliminó código duplicado y archivos inconsistentes con la versión local

---

## 🎯 Objetivos Futuros

- ✅ Expandir la API a 100 ciudades alrededor del mundo
- ✅ Generar archivos CSV "crudos" diarios como respaldo
- 🧠 Integrar IA con TensorFlow para predicción meteorológica
- 📦 Rediseñar la arquitectura hacia microservicios

---

## 📦 Endpoints Disponibles

| Método                               | Endpoint             | Descripción                                           |
| ------------------------------------ | -------------------- | ----------------------------------------------------- |
| GET                                  | `/weather/{city}`    | Obtiene datos climáticos actuales para una ciudad     |
| POST                                 | `/weather/fetch_all` | Ejecuta manualmente el módulo de recolección de datos |
| Para todas las ciudades configuradas |
| GET                                  | `/export`            | Exporta manualmente el CSV del día actual             |

---

## 🐳 Despliegue con Docker Compose

```bash
# Construir e iniciar contenedores
$ docker-compose up --build
```

Esto levantará tanto la API como el script recurrente de recolección (`schedule.py`).

---

## 📁 Exportación de Datos

- Exportación automática diaria con nombre `YYYY-MM-DD.csv`
- Archivos generados en la raíz o en una carpeta `exports/`
- Preparado para alimentar proyectos de limpieza (`Clean-data`) y entrenamiento de IA

---

## 🧠 Proyecto Vinculado: Clean-data

Proyecto paralelo encargado de:

- -- En proceso--
- Recibir archivos CSV generados por SkyNow
- Limpiar y dividir los datos por ciudad
- Preparar los datos para análisis y entrenamiento de modelos de IA

---

## 🧑‍💻 Autor

**MiloDev** - Desarrollador de software futuro software engineer, backend, análisis de datos, automatización e IA.

GitHub: [Zp07](https://github.com/Zp07)

---
