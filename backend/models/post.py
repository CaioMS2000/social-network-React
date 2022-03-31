#Ormar
import ormar
from datetime import datetime

from ._metaclass import _Meta
from.user import User

class Post(ormar.Model):
    class Meta(_Meta):
        pass

    id = ormar.Integer(primary_key=True, index=True, autoincrement=True)
    user_id = ormar.ForeignKey(User, primary_key=True, index=True)
    created_at = ormar.DateTime(default=datetime.now)
    image = ormar.Text(default="#")
    inner_text = ormar.Text(max_length=1000, default="")

# just SQLAlchemy
"""
import sqlalchemy
import sqlalchemy.orm
from datetime import datetime

import _database

class Post(_database.Base):
    __tablename__="posts"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), primary_key=True, index=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now())
    image = sqlalchemy.Column(sqlalchemy.Text, default="#")
    inner_text = sqlalchemy.Column(sqlalchemy.String(1000), default="")
    comment = sqlalchemy.orm.relationship("Comment")
    likes = sqlalchemy.orm.relationship("Like")
"""