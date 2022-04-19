import typing
import pydantic

from .metaclasses import CONFIG
from .message import Message

class ChatBase(pydantic.BaseModel):
    first_id: int
    second_id: int


class ChatCreate(ChatBase):
    class Config(CONFIG):
        pass


class Chat(ChatBase):
    id: int
    class Config(CONFIG):
        pass