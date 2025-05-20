from fastapi import FastAPI, Request
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
def status():
    return {
        "status": "online",
        "engine": "Resolver IA v4.1",
        "author": "Kabir Hazbún"
    }

@app.get("/resolver")
async def resolver(q: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un modelo experto en estrategia avanzada, lógica y análisis táctico"},
                {"role": "user", "content": q}
            ]
        )
        return {"respuesta": response["choices"][0]["message"]["content"]}
    except Exception as e:
        return {"error": str(e)}
