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
    res = {
        "status" : "ok",
        "message" : f"""API is running with user: {os.getenv("MONGODB_USER")}"""
    }
    return res