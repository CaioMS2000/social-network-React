import sqlalchemy
import sqlalchemy.orm
from datetime import datetime

import database

class Message(database.Base):
    __tablename__="messages"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True, autoincrement=True)
    conversation_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("conversations.id"), primary_key=True, index=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now())
    inner_text = sqlalchemy.Column(sqlalchemy.String(1000), default="")
    read = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    image = sqlalchemy.Column(sqlalchemy.Text, default="#")