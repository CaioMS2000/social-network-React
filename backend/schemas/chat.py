import typing
import pydantic

from .metaclasses import CONFIG
from .message import Message

class ChatBase(pydantic.BaseModel):
    messages: typing.List[Message]
    id: int
    first_id: int
    second_id: int


class ChatCreate(ChatBase):
    class Config(CONFIG):
        pass


class Chat(ChatBase):
    class Config(CONFIG):
        pass