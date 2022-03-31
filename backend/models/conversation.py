#Ormar
import ormar

from ._metaclass import _Meta
from .user import User

class Conversation(ormar.Model):
    class Meta(_Meta):
        pass

    first_id = ormar.ForeignKey(User, primary_key=True)
    second_id = ormar.ForeignKey(User, primary_key=True)
    id = ormar.Integer( primary_key=True, index=True, autoincrement=True)

# just SQLAlchemy
"""
import sqlalchemy
import sqlalchemy.orm
from datetime import datetime

import _database

class Conversation(_database.Base):
    __tablename__="conversations"
    first_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), primary_key=True, index=True)
    second_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), primary_key=True, index=True)
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True, autoincrement=True)
    messages = sqlalchemy.orm.relationship("Message")
"""