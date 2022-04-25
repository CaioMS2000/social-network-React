from database import _database
from database import _metadata

class META():
    database = _database
    metadata = _metadata
"""
class _META(ormar.Model):
    class META:
        database = db.database
        metadata = db.metadata
"""