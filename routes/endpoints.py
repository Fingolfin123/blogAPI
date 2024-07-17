from fastapi import APIRouter

# Inti the API router for end point wrapper
entry_root = APIRouter()

# Endpoint
@entry_root.get("/") # main route
def apiRunning():
    res = {
        "status" : "ok",
        "message" : "API is running"
    }
    return res