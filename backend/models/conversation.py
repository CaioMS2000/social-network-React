import sqlalchemy
import sqlalchemy.orm
from datetime import datetime

import database

class Conversation(database.Base):
    __tablename__="conversations"
    first_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), primary_key=True, index=True)
    second_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), primary_key=True, index=True)
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True, autoincrement=True)
    messages = sqlalchemy.orm.relationship("Message")