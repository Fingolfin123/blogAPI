from fastapi import FastAPI
from routes.endpoints import entry_root
from routes.blog_routes import blog_root

# Initialize the application
app = FastAPI()

app.include_router(entry_root)
app.include_router(blog_root)