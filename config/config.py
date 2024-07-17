
from pymongo.mongo_client import MongoClient
import os

# Create a new client and connect to the server
MONGODB_URL = "mongodb+srv://bengisla123:6KUJ4nf7mKNUowBZ@cluster0.voqjoar.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# print(os.getenv("MONGODB_URL"))
# client = MongoClient(os.getenv("MONGODB_URL"))
client = MongoClient(MONGODB_URL)
db = client.blogAPI
blog_collection = db["Blogs"]


# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
