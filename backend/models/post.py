import sqlalchemy
import sqlalchemy.orm
from datetime import datetime

import database

class Post(database.Base):
    __tablename__="posts"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), primary_key=True, index=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now())
    image = sqlalchemy.Column(sqlalchemy.Text, default="#")
    inner_text = sqlalchemy.Column(sqlalchemy.String(1000), default="")
    comment = sqlalchemy.orm.relationship("Comment")
    likes = sqlalchemy.orm.relationship("Like")