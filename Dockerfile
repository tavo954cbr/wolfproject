# Dockerfile

# Imagen base
FROM python:3.13-slim

# Establecer directorio de trabajo
WORKDIR /sellers

# Copiar archivos necesarios
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY sellers/ .

# Exponer el puerto por donde correrá el servidor
EXPOSE 8000

# Comando por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
