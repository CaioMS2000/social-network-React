from datetime import datetime

from ._metaclasses import _BASECLASS, _CREATIONCLASS

class FriendshipBase(_BASECLASS):
    pass


class FriendshipCreate(FriendshipBase, _CREATIONCLASS):
    pass


class Friendship(FriendshipBase, _CREATIONCLASS):
    receiver_id: int
    sender_id: int
    created_at: str