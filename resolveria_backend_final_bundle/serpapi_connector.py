
import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SERPAPI_KEY")

def buscar_google(query):
    search = GoogleSearch({
        "q": query,
        "api_key": API_KEY
    })
    return search.get_dict()

def buscar_noticias(query):
    search = GoogleSearch({
        "engine": "google_news",
        "q": query,
        "api_key": API_KEY
    })
    return search.get_dict()

def buscar_scholar(query):
    search = GoogleSearch({
        "engine": "google_scholar",
        "q": query,
        "api_key": API_KEY
    })
    return search.get_dict()
