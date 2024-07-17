# FastAPI Blog Application

This is a simple blog application built with FastAPI and MongoDB Atlas. It allows users to perform CRUD (Create, Read, Update, Delete) operations on blog posts.

## Features

- Create a new blog post
- Read all blog posts
- Read a single blog post by ID
- Update a blog post by ID
- Delete a blog post by ID

## Requirements

- Python 3.8+
- FastAPI
- PyMongo
- Uvicorn (ASGI server)
- MongoDB Atlas account

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/fastapi-blog.git
    cd fastapi-blog
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Set up your MongoDB Atlas connection string in a `.env` file:

    ```env
    MONGO_CONNECTION_STRING=mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority
    ```

## Usage

1. Run the FastAPI application:

    ```sh
    uvicorn main:app --reload
    ```

2. Open your browser and go to `http://127.0.0.1:8000/docs` to access the interactive API documentation.


