from pydantic import BaseModel
from typing import List, Optional


class BlogModel(BaseModel):
    """
    Base model for blog data.

    Attributes:
        title (str): The title of the blog post.
        sub_title (str): The subtitle of the blog post.
        content (str): The content of the blog post.
        author (str): The author of the blog post.
        tags (List[str]): A list of tags associated with the blog post.
    """
    title: str
    sub_title: str
    content: str
    author: str
    tags: List[str]


class UpdateBlogModel(BaseModel):
    """
    Model for updating blog data.

    Attributes:
        title (Optional[str]): The title of the blog post.
        sub_title (Optional[str]): The subtitle of the blog post.
        content (Optional[str]): The content of the blog post.
        author (Optional[str]): The author of the blog post.
        tags (Optional[List[str]]): A list of tags associated with the blog post.
    """
    title: Optional[str] = None
    sub_title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    tags: Optional[List[str]] = None
