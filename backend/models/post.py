import ormar
from datetime import datetime

from ._metaclass import META
from.user import User

class Post(ormar.Model):
    class Meta(META):
        # constraints = [ormar.PrimaryKeyConstraint("id", "user_id")]
        pass

    id = ormar.Integer(primary_key=True, index=True, autoincrement=True)
    # user_id = ormar.ForeignKey(User, primary_key=True, index=True)
    user_id = ormar.ForeignKey(User, index=True)
    created_at = ormar.DateTime(default=datetime.now)
    image = ormar.Text(default="#")
    inner_text = ormar.Text(max_length=1000, default="")
