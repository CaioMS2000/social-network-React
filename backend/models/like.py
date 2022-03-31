#Ormar
import ormar
from datetime import datetime

from ._metaclass import _Meta
from .user import User
from .post import Post

class Like(ormar.Model):
    class Meta(_Meta):
        pass

    id = ormar.Integer(primary_key=True, index=True, autoincrement=True)
    post_id = ormar.ForeignKey(Post, primary_key=True, index=True)
    user_id = ormar.ForeignKey(User, primary_key=True, index=True)
    created_at = ormar.DateTime(default=datetime.now)

# just SQLAlchemy
"""
import sqlalchemy
import sqlalchemy.orm
from datetime import datetime

import _database

class Like(_database.Base):
    __tablename__="likes"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True, autoincrement=True)
    post_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("posts.id"), primary_key=True, index=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), primary_key=True, index=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now())
"""