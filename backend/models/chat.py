import ormar

from ._metaclass import META
from .user import User

class Chat(ormar.Model):
    class Meta(META):
        # constraints = [ormar.PrimaryKeyConstraint("id", "first_id", "second_id")]
        pass

    # first_id = ormar.ForeignKey(User, primary_key=True)
    # second_id = ormar.ForeignKey(User, primary_key=True)
    first_id = ormar.ForeignKey(User, related_name="chat_A_side")
    second_id = ormar.ForeignKey(User, related_name="chat_B_side")
    id = ormar.Integer( primary_key=True, index=True, autoincrement=True)
