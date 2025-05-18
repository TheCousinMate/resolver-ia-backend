
from fastapi import FastAPI, UploadFile, File, Query
from fastapi.middleware.cors import CORSMiddleware
from serpapi_connector import buscar_google, buscar_noticias, buscar_scholar
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

app = FastAPI(
    title="Resolver IA API",
    description="API oficial de Resolver IA con integración SerpApi (Google, News, Scholar)",
    version="2.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Resolver IA backend activo con SerpApi"}

@app.get("/buscar/google")
def google_search(q: str = Query(..., description="Término de búsqueda")):
    return buscar_google(q)

@app.get("/buscar/noticias")
def news_search(q: str = Query(..., description="Término de búsqueda de noticias")):
    return buscar_noticias(q)

@app.get("/buscar/scholar")
def scholar_search(q: str = Query(..., description="Término de búsqueda académica")):
    return buscar_scholar(q)

@app.post("/analyze")
def analyze(file: UploadFile = File(...)):
    content = file.file.read().decode("utf-8")
    lines = content.splitlines()
    return {
        "filename": file.filename,
        "lines": len(lines),
        "preview": lines[:5]
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=7860, reload=True)
