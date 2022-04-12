import ormar
from datetime import datetime
from json import dumps

from ._metaclass import META
from .chat import Chat
from .user import User
from custom.Data_serializer import json_serial

class Message(ormar.Model):
    class Meta(META):
        # constraints = [ormar.PrimaryKeyConstraint("id", "user_id", "chat_id")]
        pass

    id = ormar.Integer(primary_key=True, index=True, autoincrement=True)
    # chat_id = ormar.ForeignKey(Chat, primary_key=True, index=True)
    # user_id = ormar.ForeignKey(User, primary_key=True, index=True)
    chat_id = ormar.ForeignKey(Chat, index=True)
    user_id = ormar.ForeignKey(User, index=True)
    # created_at = ormar.DateTime(default=datetime.now)
    # created_at = ormar.DateTime(default=dumps(datetime.now(), default=json_serial))
    created_at = ormar.String(max_length=30, default=dumps(datetime.now(), default=json_serial))
    inner_text = ormar.Text(max_length=1000, default="")
    read = ormar.Boolean(default=False)
    image = ormar.Text(default="#")
