from fastapi import APIRouter
from models.blog import BlogModel

# Inti the API router for blog wrapper
blog_root = APIRouter()

# post request
@blog_root.post("/new/blog")
def NewBlog(doc:BlogModel):  # make sure to grab expected blog model
    doc = dict(doc)
    return doc

