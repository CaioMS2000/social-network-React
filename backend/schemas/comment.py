from datetime import datetime

from ._metaclasses import _BASECLASS, _CREATIONCLASS

class CommentBase(_BASECLASS):
    pass


class CommentCreate(CommentBase, _CREATIONCLASS):
    inner_text: str


class Comment(CommentBase, _CREATIONCLASS):
    id: int
    post_id: int
    user_id: int
    created_at: datetime