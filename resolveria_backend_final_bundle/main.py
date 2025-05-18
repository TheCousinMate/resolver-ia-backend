
from fastapi import FastAPI, Query
from serpapi_connector import buscar_google, buscar_noticias, buscar_scholar

app = FastAPI(
    title="Resolver IA Backend",
    description="Conexión con SerpApi y lógica de búsqueda",
    version="1.0.0"
)

@app.get("/healthz")
def health_check():
    return {"status": "ok"}

@app.get("/buscar/google")
def buscar_google_api(q: str = Query(..., description="Término de búsqueda en Google")):
    return buscar_google(q)

@app.get("/buscar/noticias")
def buscar_noticias_api(q: str = Query(..., description="Término para noticias")):
    return buscar_noticias(q)

@app.get("/buscar/scholar")
def buscar_scholar_api(q: str = Query(..., description="Búsqueda académica")):
    return buscar_scholar(q)
