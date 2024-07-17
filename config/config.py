
from pymongo.mongo_client import MongoClient
import os

# Create a new client and connect to the server
MONGODB_URL = "mongodb+srv://bengisla123:6KUJ4nf7mKNUowBZ@cluster0.voqjoar.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# TODO: change url to env variable, debug os.getenv()
# client = MongoClient(os.getenv("MONGODB_URL"))
client = MongoClient(MONGODB_URL)
db = client.blogAPI
blog_collection = db["Blogs"]

