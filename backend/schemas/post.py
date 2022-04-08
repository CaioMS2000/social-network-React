from datetime import datetime

from ._metaclasses import _BASECLASS, _CREATIONCLASS

class PostBase(_BASECLASS):
    pass

class PostCreate(PostBase, _CREATIONCLASS):
    image: str
    inner_text: str


class Post(PostBase, _CREATIONCLASS):
    id: int
    user_id: int
    created_at: str