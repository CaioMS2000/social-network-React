import pydantic

from .metaclasses import CONFIG

class FriendshipBase(pydantic.BaseModel):
    receiver_id: int
    sender_id: int


class FriendshipCreate(FriendshipBase):
    class Config(CONFIG):
        pass


class Friendship(FriendshipCreate):
    created_at: str
    
    class Config(CONFIG):
        pass