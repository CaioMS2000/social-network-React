from datetime import datetime

from ._metaclasses import _BASECLASS, _CREATIONCLASS

class MessageBase(_BASECLASS):
    read: bool


class MessageCreate(MessageBase, _CREATIONCLASS):
    inner_text: str


class Message(MessageBase, _CREATIONCLASS):
    id: int
    chat_id: int
    created_at: datetime