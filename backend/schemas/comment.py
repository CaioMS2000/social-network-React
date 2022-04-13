import pydantic

from .metaclasses import CONFIG

class CommentBase(pydantic.BaseModel):
    id: int
    post_id: int
    user_id: int
    created_at: str
    inner_text: str


class CommentCreate(CommentBase):
    class Config(CONFIG):
        pass


class Comment(CommentBase):
    class Config(CONFIG):
        pass