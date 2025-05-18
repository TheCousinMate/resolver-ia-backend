
import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def buscar_google(query, num=10):
    params = {
        "engine": "google",
        "q": query,
        "num": num,
        "api_key": SERPAPI_KEY
    }
    search = GoogleSearch(params)
    return search.get("organic_results", [])

def buscar_noticias(query, num=10):
    params = {
        "engine": "google_news",
        "q": query,
        "api_key": SERPAPI_KEY
    }
    search = GoogleSearch(params)
    return search.get("news_results", [])

def buscar_scholar(query, num=10):
    params = {
        "engine": "google_scholar",
        "q": query,
        "api_key": SERPAPI_KEY
    }
    search = GoogleSearch(params)
    return search.get("organic_results", [])

def buscar_trends(query):
    params = {
        "engine": "google_trends",
        "q": query,
        "api_key": SERPAPI_KEY
    }
    search = GoogleSearch(params)
    return search.get("trending_searches", [])
