from fastapi import FastAPI
import httpx
import os

app = FastAPI()

API_URL = "https://api.publicapis.org/entries?category=Science&https=true"  # API pública alternativa

@app.get("/resolver-info")
async def get_resolver_info():
    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL)
        data = response.json()
        return {"message": "Resolver IA - Datos Externos", "data": data.get("entries", [])[:5]}
