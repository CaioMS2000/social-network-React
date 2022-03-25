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