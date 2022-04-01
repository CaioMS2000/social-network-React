import ormar
from datetime import datetime

from ._metaclass import META
from .chat import Chat
from .user import User

class Message(ormar.Model):
    class Meta(META):
        # constraints = [ormar.PrimaryKeyConstraint("id", "user_id", "chat_id")]
        pass

    id = ormar.Integer(primary_key=True, index=True, autoincrement=True)
    # chat_id = ormar.ForeignKey(Chat, primary_key=True, index=True)
    # user_id = ormar.ForeignKey(User, primary_key=True, index=True)
    chat_id = ormar.ForeignKey(Chat, index=True)
    user_id = ormar.ForeignKey(User, index=True)
    created_at = ormar.DateTime(default=datetime.now)
    inner_text = ormar.Text(max_length=1000, default="")
    read = ormar.Boolean(default=False)
    image = ormar.Text(default="#")
