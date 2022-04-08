import ormar
from datetime import datetime
from json import dumps

from ._metaclass import META
from .user import User
from Data_serializer import json_serial

class Friendship(ormar.Model):
    class Meta(META):
        # constraints = [ormar.PrimaryKeyConstraint("id", "sender_id", "receiver_id")]
        pass

    id = ormar.Integer(primary_key=True, autoincrement=True)
    # sender_id = ormar.ForeignKey(User, primary_key=True, index=True)
    # receiver_id = ormar.ForeignKey(User, primary_key=True, index=True)
    sender_id = ormar.ForeignKey(User, related_name="friendship_A_side", index=True)
    receiver_id = ormar.ForeignKey(User, related_name="friendship_B_side", index=True)
    # created_at = ormar.DateTime(default=datetime.now)
    # created_at = ormar.DateTime(default=dumps(datetime.now(), default=json_serial))
    created_at = ormar.String(max_length=30, default=dumps(datetime.now(), default=json_serial))
