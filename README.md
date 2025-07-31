
# 🐺 WOLFPROJECT – Gestión de Productos

Microservicio REST desarrollado con **Django REST Framework**, con base de datos SQLite, Dockerizado y con pruebas básicas.

---

##  Estructura del proyecto

```
WOLFPROJECT/
│
├── sellers/
│   ├── productos/            # App de productos
│   ├── sellers/              # Configuración del proyecto Django
│   ├── db.sqlite3            # Base de datos local
│   └── manage.py             # Script de administración
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

##  Requisitos

- Python 3.10 o superior
- Docker y Docker Compose
- Git

---

##  Instalación local (sin Docker)

1. **Clonar el repositorio:**

```bash
git clone https://github.com/tavo954cbr/wolfproject.git
cd wolfproject
```

2. **Crear y activar un entorno virtual:**

```bash
python -m venv venv
source venv/bin/activate       # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias:**

```bash
pip install django  
pip install djangorestframework  
pip install drf-yasg #para documentacion con swagger
```

4. **Ejecutar migraciones:**

```bash
cd sellers
python manage.py migrate
```

5. **Iniciar el servidor:**

```bash
python manage.py runserver
```

Abre `http://localhost:8000/` en tu navegador.

---

##  Instalación con Docker

1. **Construir e iniciar los contenedores:**

```bash
docker-compose up --build
```

2. **Acceder a la app:**

Abre `http://localhost:8000/`

---

## 🗄️ Migraciones (con Docker)

Si necesitas ejecutar migraciones manualmente dentro del contenedor:

```bash
docker-compose exec web python manage.py migrate
```

---

## Ejecutar pruebas

### Local:
```bash
cd sellers
python manage.py test
```

### Con Docker:
```bash
docker-compose exec web python manage.py test
```

---

##  Documentación de la API

Usando Django REST Framework:

- Swagger: `http://localhost:8000/swagger/`
- Redoc: `http://localhost:8000/redoc/`

> Asegúrate de haber instalado e integrado `drf-yasg` si usas Swagger.

---

##  Endpoints disponibles

| Método | Endpoint              | Descripción               |
|--------|-----------------------|---------------------------|
| GET    | /api/productos/       | Lista todos los productos |
| POST   | /api/productos/       | Crea un nuevo producto    |
| GET    | /api/productos/{id}/  | Obtiene un producto       |
| PUT    | /api/productos/{id}/  | Actualiza un producto     |
| DELETE | /api/productos/{id}/  | Elimina un producto       |

---

##  Autor

- **GUSTAVO HERNANDEZ MARTINEZ**
- Contacto: tavo_razielsd@gmail
