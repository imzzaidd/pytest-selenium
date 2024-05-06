FROM python:3.12.3

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requisitos al contenedor
COPY requirements.txt .

# Instala las dependencias del sistema necesarias
RUN apt-get update && \
    apt-get install -y xvfb pulseaudio && \
    apt-get clean

# Instala las dependencias especificadas en el archivo de requisitos
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del directorio actual al directorio de trabajo en el contenedor
COPY . .

# Define las variables de entorno para Selenium (URL del hub y navegador)
ENV SELENIUM_HUB_URL=http://seleniumhub:4444/wd/hub
ENV SE_EVENT_BUS_HOST=$SELENIUM_HUB_URL
ENV BROWSER=firefox

# Ejecuta pytest cuando se inicie el contenedor
CMD ["pytest"]
