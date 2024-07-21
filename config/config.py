
from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv, dotenv_values

# Create a new client and connect to the server
load_dotenv()

# Retrieve the MongoDB URL from environment variables
mongodb_url = os.getenv("MONGODB_URL")

# Initialize MongoDB client
try:
    client = MongoClient(mongodb_url)
    # client.admin.command('ping')
    db = client.blogAPI
    blog_collection = db["Blogs"]
    print("MongoDB connection successful.")
except Exception as e:
    print("Error connecting to MongoDB:", e)
