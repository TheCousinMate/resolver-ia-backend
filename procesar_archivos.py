from langchain_community.document_loaders import TextLoader
import os

RUTAS = {
    "Estrategia": "Estrategia",
    "Conflictos": "Conflictos",
    "Criptografía": "Criptografía",
    "Datos y Probabilidad": "Datos y Probabilidad",
    "Ética y Comportamiento": "Ética y Comportamiento",
    "Juegos y Toma de Decisiones": "Juegos y Toma de Decisiones",
    "Otros": "Otros"
}

for categoria, carpeta in RUTAS.items():
    path = os.path.join(os.getcwd(), carpeta)
    if os.path.exists(path):
        for archivo in os.listdir(path):
            if archivo.endswith(".txt"):
                try:
                    ruta = os.path.join(path, archivo)
                    # Abrir manualmente para detectar errores
                    with open(ruta, encoding="utf-8", errors="ignore") as f:
                        texto = f.read()
                    loader = TextLoader(ruta, encoding="utf-8")
                    loader.load()
                except Exception as e:
                    print(f"Error leyendo {archivo}: {e}")
