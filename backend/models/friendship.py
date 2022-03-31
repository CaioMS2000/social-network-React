#Ormar
import ormar
from datetime import datetime

from ._metaclass import _Meta
from .user import User

class Friendship(ormar.Model):
    class Meta(_Meta):
        pass

    sender_id = ormar.ForeignKey(User, primary_key=True, index=True)
    receiver_id = ormar.ForeignKey(User, primary_key=True, index=True)
    created_at = ormar.DateTime(default=datetime.now)

# just SQLAlchemy
"""
import sqlalchemy
import sqlalchemy.orm
from datetime import datetime

import _database

class Friendship(_database.Base):
    __tablename__="friendships"
    sender_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), primary_key=True, index=True)
    receiver_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), primary_key=True, index=True)
    sender = sqlalchemy.orm.relationship("User", foreign_keys=[sender_id])
    receiver = sqlalchemy.orm.relationship("User", foreign_keys=[receiver_id])
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now())
"""