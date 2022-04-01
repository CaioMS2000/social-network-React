from datetime import datetime
import typing

from ._metaclasses import _BASECLASS, _CREATIONCLASS
from .message import Message

class ChatBase(_BASECLASS):
    messages: typing.List[Message]


class ChatCreate(ChatBase, _CREATIONCLASS):
    pass


class Chat(ChatBase, _CREATIONCLASS):
    id: int
    first_id: int
    second_id: int