from datetime import datetime

from ._metaclasses import _BASECLASS, _CREATIONCLASS

class LikeBase(_BASECLASS):
    pass


class LikeCreate(LikeBase, _CREATIONCLASS):
    pass


class Like(LikeBase, _CREATIONCLASS):
    id: int
    post_id: int
    user_id: int
    created_at: datetime