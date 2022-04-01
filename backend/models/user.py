import ormar
import passlib.hash
from datetime import datetime

from ._metaclass import META

class User(ormar.Model):
    class Meta(META):
        # constraints = [ormar.PrimaryKeyConstraint("id", "username", "email")]
        pass

    id = ormar.Integer(primary_key=True, index=True, autoincrement=True)
    # username = ormar.Text(max_length=256, primary_key=True, index=True)
    # email = ormar.Text(max_length=256, primary_key=True, index=True)
    username = ormar.Text(max_length=256)
    email = ormar.Text(max_length=256)
    hashed_password = ormar.Text(max_length=256)
    full_name = ormar.Text(max_length=256)
    profile_picture = ormar.Text(default="#")
    created_at = ormar.DateTime(default=datetime.now)

    def verify_password(self, password: str):
        return passlib.hash.bcrypt.verify(password, self.hashed_password)
