import sqlalchemy
import sqlalchemy.orm
from datetime import datetime

import database

class Friendship(database.Base):
    __tablename__="friendships"
    sender_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), primary_key=True, index=True)
    receiver_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), primary_key=True, index=True)
    sender = sqlalchemy.orm.relationship("User", foreign_keys=[sender_id])
    receiver = sqlalchemy.orm.relationship("User", foreign_keys=[receiver_id])
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now())