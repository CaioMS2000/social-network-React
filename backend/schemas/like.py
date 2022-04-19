import pydantic

from .metaclasses import CONFIG

class LikeBase(pydantic.BaseModel):
    post_id: int
    user_id: int


class LikeCreate(LikeBase):
    class Config(CONFIG):
        pass


class Like(LikeBase):
    id: int
    created_at: str
    
    class Config(CONFIG):
        pass