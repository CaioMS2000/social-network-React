import ormar
from datetime import datetime

from ._metaclass import META
from .user import User

class Friendship(ormar.Model):
    class Meta(META):
        # constraints = [ormar.PrimaryKeyConstraint("id", "sender_id", "receiver_id")]
        pass

    id = ormar.Integer(primary_key=True, autoincrement=True)
    # sender_id = ormar.ForeignKey(User, primary_key=True, index=True)
    # receiver_id = ormar.ForeignKey(User, primary_key=True, index=True)
    sender_id = ormar.ForeignKey(User, related_name="friendship_A_side", index=True)
    receiver_id = ormar.ForeignKey(User, related_name="friendship_B_side", index=True)
    created_at = ormar.DateTime(default=datetime.now)
