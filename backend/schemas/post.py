import pydantic

from .metaclasses import CONFIG

class PostBase(pydantic.BaseModel):
    inner_text: str
    id: int
    user_id: int
    created_at: str

class PostCreate(PostBase):
    image: str

    class Config(CONFIG):
        pass


class Post(PostBase):
    class Config(CONFIG):
        pass