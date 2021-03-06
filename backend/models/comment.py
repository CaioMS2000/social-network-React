import ormar
from datetime import datetime
from json import dumps

from ._metaclass import META
from  .user import User
from .post import Post
from custom.Data_serializer import json_serial

class Comment(ormar.Model):
    class Meta(META):
        # constraints = [ormar.PrimaryKeyConstraint("id", "user_id", "post_id")]
        pass

    id = ormar.Integer(primary_key=True, autoincrement=True, index=True)
    # user_id = ormar.ForeignKey(User, primary_key=True)
    # post_id = ormar.ForeignKey(Post, primary_key=True)
    user_id = ormar.ForeignKey(User)
    post_id = ormar.ForeignKey(Post)
    # created_at = ormar.DateTime(default=datetime.now)
    # created_at = ormar.DateTime(default=dumps(datetime.now(), default=json_serial))
    created_at = ormar.String(max_length=30, default=dumps(datetime.now(), default=json_serial))
    inner_text = ormar.String(max_length=100, default="")
