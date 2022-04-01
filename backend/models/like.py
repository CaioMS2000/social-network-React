import ormar
from datetime import datetime

from ._metaclass import META
from .user import User
from .post import Post

class Like(ormar.Model):
    class Meta(META):
        # constraints = [ormar.PrimaryKeyConstraint("id", "user_id", "post_id")]
        pass

    id = ormar.Integer(primary_key=True, index=True, autoincrement=True)
    # post_id = ormar.ForeignKey(Post, primary_key=True, index=True)
    # user_id = ormar.ForeignKey(User, primary_key=True, index=True)
    post_id = ormar.ForeignKey(Post, index=True)
    user_id = ormar.ForeignKey(User, index=True)
    created_at = ormar.DateTime(default=datetime.now)
