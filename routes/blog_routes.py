from fastapi import APIRouter
from models.blog import BlogModel, UpdateBlogModel
from config.config import blog_collection
from serializer.blog_serializers import decode_blog, decode_blogs
import datetime
from bson import ObjectId

# Initialize the API router for blog operations
blog_root = APIRouter()

@blog_root.post("/new/blog")
def new_blog(doc: BlogModel):
    """
    Create a new blog post.

    Args:
        doc (BlogModel): The blog data.

    Returns:
        dict: Response containing status, message, and the ID of the created blog post.
    """
    doc = dict(doc)
    current_date = datetime.date.today()
    doc["date"] = str(current_date)

    res = blog_collection.insert_one(doc)
    doc_id = str(res.inserted_id)

    return {
        "status": "ok",
        "message": "Blog posted successfully",
        "_id": doc_id
    }

@blog_root.get("/all/blogs")
def all_blogs():
    """
    Get all blog posts.

    Returns:
        dict: Response containing status and the list of all blog posts.
    """
    res = blog_collection.find()
    decoded_data = DecodeBlogs(res)
    return {
        "status": "ok",
        "data": decoded_data
    }

@blog_root.get("/blog/{_id}")
def get_blog(_id: str):
    """
    Get a specific blog post by ID.

    Args:
        _id (str): The ID of the blog post.

    Returns:
        dict: Response containing status and the blog post data.
    """
    res = blog_collection.find_one({"_id": ObjectId(_id)})
    decoded_blog = DecodeBlog(res)
    return {
        "status": "ok",
        "data": decoded_blog
    }

@blog_root.patch("/update/{_id}")
def update_blog(_id: str, doc: UpdateBlogModel):
    """
    Update a specific blog post by ID.

    Args:
        _id (str): The ID of the blog post.
        doc (UpdateBlogModel): The updated blog data.

    Returns:
        dict: Response containing status and message.
    """
    req = dict(doc.model_dump(exclude_unset=True))
    
    blog_collection.find_one_and_update(
        {"_id": ObjectId(_id)},
        {"$set": req}
    )

    return {
        "status": "ok",
        "message": "Blog updated successfully"
    }

@blog_root.delete("/delete/{_id}")
def delete_blog(_id: str):
    """
    Delete a specific blog post by ID.

    Args:
        _id (str): The ID of the blog post.

    Returns:
        dict: Response containing status and message.
    """
    blog_collection.find_one_and_delete(
        {"_id": ObjectId(_id)}
    )

    return {
        "status": "ok",
        "message": "Blog deleted successfully"
    }
