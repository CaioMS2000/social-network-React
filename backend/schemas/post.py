import pydantic

from .metaclasses import CONFIG

class PostBase(pydantic.BaseModel):
    inner_text: str
    user_id: int

class PostCreate(PostBase):
    class Config(CONFIG):
        pass


class Post(PostBase):
    image: str
    id: int
    created_at: str

    class Config(CONFIG):
        pass