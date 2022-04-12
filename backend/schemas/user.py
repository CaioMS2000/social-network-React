from datetime import datetime

from ._metaclasses import _BASECLASS, _CREATIONCLASS

class UserBase(_BASECLASS):
    email: str
    full_name: str
    username: str


class UserCreate(UserBase, _CREATIONCLASS):
    hashed_password: str


class User(UserCreate, _CREATIONCLASS):
    id: int
    created_at: str
    profile_picture: str
