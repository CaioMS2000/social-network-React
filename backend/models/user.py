import sqlalchemy
import sqlalchemy.orm
import passlib.hash
from datetime import datetime

import database

class User(database.Base):
    __tablename__="users"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True, autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.String(256), primary_key=True, index=True)
    email = sqlalchemy.Column(sqlalchemy.String(256), primary_key=True, index=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String(256))
    full_name = sqlalchemy.Column(sqlalchemy.String(256))
    profile_picture = sqlalchemy.Column(sqlalchemy.Text, default="#")
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now())
    posts = sqlalchemy.orm.relationship("Post")
    friends = sqlalchemy.orm.relationship("Friendship")

    def verify_password(self, password: str):
        return passlib.hash.bcrypt.verify(password, self.hashed_password)