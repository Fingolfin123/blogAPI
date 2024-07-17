def decode_blog(doc: dict) -> dict:
    """
    Serialize a single blog document.

    Args:
        doc (dict): The blog document.

    Returns:
        dict: The serialized blog document.
    """
    return {
        "_id": str(doc["_id"]),
        "title": doc["title"],
        "sub_title": doc["sub_title"],
        "content": doc["content"],
        "author": doc["author"],
        "date": doc["date"]
    }


def decode_blogs(docs: list) -> list:
    """
    Serialize a list of blog documents.

    Args:
        docs (list): The list of blog documents.

    Returns:
        list: The list of serialized blog documents.
    """
    return [decode_blog(doc) for doc in docs]
