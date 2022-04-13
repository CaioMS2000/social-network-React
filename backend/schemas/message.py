import pydantic

from .metaclasses import CONFIG

class MessageBase(pydantic.BaseModel):
    read: bool
    id: int
    chat_id: int
    created_at: str
    inner_text: str


class MessageCreate(MessageBase):
    class Config(CONFIG):
        pass


class Message(MessageBase):
    class Config(CONFIG):
        pass