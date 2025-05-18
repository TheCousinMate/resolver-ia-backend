
# Resolver IA Backend

Este backend proporciona servicios de análisis estratégico, búsqueda externa en tiempo real, lógica aplicada y procesamiento de archivos para el modelo Resolver IA.

## 🚀 Funcionalidades

- 🔍 Búsqueda en Google, Noticias y Google Scholar (vía SerpApi)
- 📎 Subida y análisis de archivos de texto
- 📊 Matriz de decisiones y lógica argumentativa
- 🌐 API REST construida con FastAPI
- 🐳 Desplegable vía Docker o Render.com

---

## 📂 Estructura del proyecto

```
resolver-ia-backend/
│
├── main.py                  # Backend principal
├── serpapi_connector.py     # Módulo de conexión externa
├── .env.example             # Variables de entorno (modelo)
├── requirements.txt         # Dependencias
├── Dockerfile               # Contenedor para despliegue
└── README.md                # Este archivo
```

---

## 🔑 Variables de entorno requeridas

Copia `.env.example` como `.env` y completa con tus datos reales.

```
SERPAPI_KEY=TU_API_KEY
ACCOUNT_EMAIL=tu_email@ejemplo.com
PLAN_NAME=Cloud 8M
TOTAL_QUOTA=100000000
API_BASE_URL=https://serpapi.com/search
```

---

## 🚀 Despliegue local

```bash
uvicorn main:app --reload --port 7860
```

## ☁️ Despliegue en Render

1. Crea repositorio en GitHub y sube este proyecto
2. En Render.com → Create Web Service → Conecta GitHub
3. Usa puerto `7860`, runtime `Python 3`, start command: `python main.py`
4. Agrega tus variables de entorno

---

## ✍️ Autor

Kabir Hazbún C. – 2025
