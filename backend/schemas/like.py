import pydantic

from .metaclasses import CONFIG

class LikeBase(pydantic.BaseModel):
    id: int
    post_id: int
    user_id: int
    created_at: str


class LikeCreate(LikeBase):
    class Config(CONFIG):
        pass


class Like(LikeBase):
    class Config(CONFIG):
        pass