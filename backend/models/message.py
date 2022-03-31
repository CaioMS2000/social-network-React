#Ormar
import ormar
from datetime import datetime

from ._metaclass import _Meta
from .conversation import Conversation

class Message(ormar.Model):
    class Meta(_Meta):
        pass

    id = ormar.Integer(primary_key=True, index=True, autoincrement=True)
    conversation_id = ormar.ForeignKey(Conversation, primary_key=True, index=True)
    created_at = ormar.DateTime(default=datetime.now)
    inner_text = ormar.Text(max_length=1000, default="")
    read = ormar.Boolean(default=False)
    image = ormar.Text(default="#")

# just SQLAlchemy
"""
import sqlalchemy
import sqlalchemy.orm
from datetime import datetime

import _database

class Message(_database.Base):
    __tablename__="messages"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True, autoincrement=True)
    conversation_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("conversations.id"), primary_key=True, index=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now())
    inner_text = sqlalchemy.Column(sqlalchemy.String(1000), default="")
    read = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    image = sqlalchemy.Column(sqlalchemy.Text, default="#")
"""