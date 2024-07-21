from fastapi import APIRouter
import os
from dotenv import load_dotenv, dotenv_values

# Create a new client and connect to the server
load_dotenv()

# Inti the API router for end point wrapper
entry_root = APIRouter()

# Endpoint
@entry_root.get("/") # main route
def apiRunning():
    mongodb_url = os.getenv("MONGODB_URL")
    res = {
        "status" : "ok",
        "message" : mongodb_url#"API is running"
    }
    return res