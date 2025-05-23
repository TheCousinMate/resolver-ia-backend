from fastapi import FastAPI, HTTPException
import openai
import os
from dotenv import load_dotenv

load_dotenv('.env.local')

app = FastAPI()

openai.api_key = os.getenv(\"OPENAI_API_KEY\")

@app.get(\"/\")
def status():
    return {
        \"status\": \"online\",
        \"engine\": \"Resolver IA v4.1\",
        \"author\": \"Kabir Hazbún\"
    }

@app.post(\"/resolver\")
async def resolver(peticion: dict):
    pregunta = peticion.get('pregunta', '').strip()
    if not pregunta:
        raise HTTPException(status_code=422, detail=\"La pregunta no puede estar vacía\")
    try:
        response = openai.ChatCompletion.create(
            model=\"gpt-3.5-turbo\",
            messages=[
                {\"role\": \"system\", \"content\": \"Eres un modelo experto en estrategia avanzada, lógica y análisis táctico\"},
                {\"role\": \"user\", \"content\": pregunta}
            ]
        )
        return {\"respuesta\": response[\"choices\"][0][\"message\"][\"content\"]}
    except Exception:
        raise HTTPException(status_code=500, detail=\"Error interno del servidor\")
