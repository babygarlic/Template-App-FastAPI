# FastAPI Template Application
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-0.1.0-green.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688.svg)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)


A modern, scalable, and well-structured template for building web applications with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. This template is designed to be easy to set up, maintain, and extend, making it ideal for personal projects.


---


## ✨ Features

This template provides a robust foundation for building modern web applications:

- ✅ **FastAPI Framework**: Leverage the power of FastAPI for high-performance, asynchronous APIs with automatic OpenAPI documentation.
- 🔐 **JWT Authentication**: Secure user authentication with JSON Web Tokens (JWT) for protected routes.
- 🗄️ **SQLAlchemy ORM**: Efficient database management with SQLAlchemy, supporting PostgreSQL out of the box.
- 🧪 **Pydantic Validation**: Type-safe data validation and serialization using Pydantic models.
- 📁 **Modular Structure**: Clean separation of concerns with dedicated routers, models, schemas, and services.
- 🛠️ **Extensible Design**: Easily add new features, endpoints, or database models without breaking existing code.
- 🚀 **Production Ready**: Configured for scalability and deployment with environment variables and best practices.

---

## 🛠 Tech Stack

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.9+.
- **SQLAlchemy**: A powerful ORM for database operations with PostgreSQL.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **PostgreSQL**: A robust, open-source relational database.
- **JWT (PyJWT)**: Secure authentication with JSON Web Tokens.
- **Uvicorn**: ASGI server implementation for running FastAPI applications.
- **Pytest**: Testing framework for unit and integration tests.

---
## 📂 Project Structure
```text
fastapi-template/
├── app/                        # Core application code
│   ├── api/                    # API endpoints (routers)
│   │   ├── __init__.py         # Marks directory as a Python package
│   │   ├── task.py             # Task-related API endpoints (e.g., CRUD for tasks)
│   │   ├── user.py             # User-related API endpoints (e.g., user management)
│   ├── core/                   # Core configuration and utilities
│   │   ├── __init__.py         # Marks directory as a Python package
│   │   ├── config.py           # Environment variables and app settings
│   │   ├── database.py         # Database connection and session setup
│   ├── models/                 # SQLAlchemy database models
│   │   ├── task.py             # Task model for database schema
│   │   ├── user.py             # User model for database schema
│   ├── schemas/                # Pydantic schemas for data validation
│   │   ├── task_schema.py      # Task schemas for request/response validation
│   │   ├── user_schema.py      # User schemas for request/response validation
│   ├── services/               # Business logic and service layers
│   │   ├── __init__.py         # Marks directory as a Python package
│   │   ├── task_service.py     # Logic for task operations (e.g., create, update)
│   │   ├── user_service.py     # Logic for user operations (e.g., auth, profile)
│   ├── utils/                  # Utility functions and helpers
│   │   ├── __init__.py         # Marks directory as a Python package
│   │   ├── exception.py        # Custom exception classes
│   │   ├── security.py         # Security utilities (e.g., JWT, password hashing)
├── __init__.py                 # Marks app/ as a Python package
├── main.py                     # Main application entry point (FastAPI instance)
├── server.py                   # Server setup (e.g., Uvicorn configuration)
├── .env.example                # Example environment variables for configuration
├── .gitignore                  # Specifies files/folders to ignore in Git
├── .python-version             # Specifies Python version (used by tools like pyenv)
├── README.md                   # Project documentation
├── pyproject.toml              # Project metadata and dependency configuration
├── uv.lock                     # Lock file for uv (dependency manager)
```


