FastAPI JWT Authentication with Role-Based Access Control (RBAC)
Overview
This project demonstrates how to build a simple API using FastAPI, PostgreSQL, and SQLModel that handles:

User Authentication using JWT (JSON Web Tokens)

Role-Based Access Control (RBAC) where users can have different roles (e.g., admin and user)

CRUD operations for managing resources like projects

Key Features:
User Registration and Login: Users can register and log in to receive a JWT token.

JWT-based Authorization: Once logged in, the user receives a token that must be included in subsequent API requests.

Role-Based Access Control (RBAC): Users with different roles have different levels of access to the API (e.g., only admins can create, update, or delete resources).

