import pydantic

from .metaclasses import CONFIG

class FriendshipBase(pydantic.BaseModel):
    receiver_id: int
    sender_id: int
    created_at: str


class FriendshipCreate(FriendshipBase):
    class Config(CONFIG):
        pass


class Friendship(FriendshipCreate):
    class Config(CONFIG):
        pass