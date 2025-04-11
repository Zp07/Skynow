#Imagen inicial
FROM python:3.13.2

#Directorio inicial
WORKDIR /app

# Copiar solo requirements primero para aprovechar caché
COPY requirements.txt .

#Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

#Copiar las dependencias
COPY . .

#Comando iniciar app
CMD [ "uvicorn","app.main:app","--host","0.0.0.0","--port","8000" ]