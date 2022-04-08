import ormar
from datetime import datetime
from json import dumps

from ._metaclass import META
from .user import User
from .post import Post
from Data_serializer import json_serial

class Like(ormar.Model):
    class Meta(META):
        # constraints = [ormar.PrimaryKeyConstraint("id", "user_id", "post_id")]
        pass

    id = ormar.Integer(primary_key=True, index=True, autoincrement=True)
    # post_id = ormar.ForeignKey(Post, primary_key=True, index=True)
    # user_id = ormar.ForeignKey(User, primary_key=True, index=True)
    post_id = ormar.ForeignKey(Post, index=True)
    user_id = ormar.ForeignKey(User, index=True)
    # created_at = ormar.DateTime(default=datetime.now)
    # created_at = ormar.DateTime(default=dumps(datetime.now(), default=json_serial))
    created_at = ormar.String(max_length=30, default=dumps(datetime.now(), default=json_serial))
