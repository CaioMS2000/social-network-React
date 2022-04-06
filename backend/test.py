from datetime import datetime
from json import dumps
from datetime import date, datetime

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

print(f"\n{datetime.now()}")
print(dumps(datetime.now(), default=json_serial))