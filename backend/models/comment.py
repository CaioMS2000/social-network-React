import ormar
from datetime import datetime

from ._metaclass import META
from  .user import User
from .post import Post

class Comment(ormar.Model):
    class Meta(META):
        # constraints = [ormar.PrimaryKeyConstraint("id", "user_id", "post_id")]
        pass

    id = ormar.Integer(primary_key=True, autoincrement=True, index=True)
    # user_id = ormar.ForeignKey(User, primary_key=True)
    # post_id = ormar.ForeignKey(Post, primary_key=True)
    user_id = ormar.ForeignKey(User)
    post_id = ormar.ForeignKey(Post)
    created_at = ormar.DateTime(default=datetime.now)
    inner_text = ormar.String(max_length=100, default="")
