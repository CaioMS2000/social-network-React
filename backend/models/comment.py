#Ormar
import ormar
from datetime import datetime

from ._metaclass import _Meta
from  .user import User
from .post import Post

class Comment(ormar.Model):
    class Meta(_Meta):
        constraints = [ormar.PrimaryKeyConstraint("id", "user_id", "post_id")]

    id = ormar.Integer(primary_key=True, autoincrement=True, index=True)
    # post_id = ormar.Integer(primary_key=True)
    # user_id = ormar.Integer(primary_key=True)
    user_id = ormar.ForeignKey(User, primary_key=True)
    post_id = ormar.ForeignKey(Post, primary_key=True)
    created_at = ormar.DateTime(default=datetime.now)
    inner_text = ormar.String(mas_length=100, default="")

# just SQLAlchemy
"""
import sqlalchemy
import sqlalchemy.orm
from datetime import datetime

import database

class Comment(database.Base):
    __tablename__="comments"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True, autoincrement=True)
    post_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("posts.id"), primary_key=True, index=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), primary_key=True, index=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now())
    inner_text = sqlalchemy.Column(sqlalchemy.String(1000), default="")
"""