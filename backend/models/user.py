#Ormar
import ormar
import passlib.hash
from datetime import datetime

from ._metaclass import _Meta

class User(ormar.Model):
    class Meta(_Meta):
        pass

    id = ormar.Integer(primary_key=True, index=True, autoincrement=True)
    username = ormar.Text(max_length=256, primary_key=True, index=True)
    email = ormar.Text(max_length=256, primary_key=True, index=True)
    hashed_password = ormar.Text(max_length=256)
    full_name = ormar.Text(max_length=256)
    profile_picture = ormar.Text(default="#")
    created_at = ormar.DateTime(default=datetime.now)

    def verify_password(self, password: str):
        return passlib.hash.bcrypt.verify(password, self.hashed_password)

# just SQLAlchemy
"""
import sqlalchemy
import sqlalchemy.orm
import passlib.hash
from datetime import datetime

import _database

class User(_database.Base):
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
"""