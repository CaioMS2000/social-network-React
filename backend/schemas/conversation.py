from datetime import datetime
import typing

from ._metaclasses import _BASECLASS, _CREATIONCLASS
from .message import Message

class ConversationBase(_BASECLASS):
    messages: typing.List[Message]


class ConversationCreate(ConversationBase, _CREATIONCLASS):
    pass


class Conversation(ConversationBase, _CREATIONCLASS):
    id: int
    first_id: int
    second_id: int