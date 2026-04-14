# MediaFlow API

A FastAPI-based backend for a photo and video sharing platform.  
This project supports user authentication, media uploads, and CRUD operations for posts.

## Features

- User registration and login
- JWT-based authentication
- Upload photos and videos
- Create, read, and delete posts
- FastAPI auto-generated interactive API docs
- Modular backend structure
- Ready for local development and deployment

## Tech Stack

- FastAPI
- Python
- PostgreSQL or SQLite
- SQLAlchemy
- JWT authentication
- ImageKit for media storage
- Uvicorn

## Project Structure

```bash
.
├── app/
│   ├── main.py
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── utils/
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md