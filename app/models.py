from sqlmodel import SQLModel, Field
from typing import Optional
from enum import Enum

class Role(str, Enum):
    user = "user"
    admin = "admin"

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    hashed_password: str
    role: Role = Field(default=Role.user)

class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str

