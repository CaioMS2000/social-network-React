import pydantic

from .metaclasses import CONFIG

class MessageBase(pydantic.BaseModel):
    chat_id: int
    user_id: int
    inner_text: str


class MessageCreate(MessageBase):
    class Config(CONFIG):
        pass


class Message(MessageBase):
    read: bool
    id: int
    created_at: str

    class Config(CONFIG):
        pass