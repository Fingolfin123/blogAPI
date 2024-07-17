from pydantic import BaseModel

# Init the base model of the blog data
class BlogModel(BaseModel):
    title: str
    content : str
    author : str
    tags : list
    