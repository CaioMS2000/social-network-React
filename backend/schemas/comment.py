import pydantic

from .metaclasses import CONFIG

class CommentBase(pydantic.BaseModel):
    post_id: int
    user_id: int
    inner_text: str


class CommentCreate(CommentBase):
    class Config(CONFIG):
        pass


class Comment(CommentBase):
    id: int
    created_at: str
    
    class Config(CONFIG):
        pass