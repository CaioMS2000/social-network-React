from datetime import datetime
from json import dumps
from datetime import date, datetime
import builtins


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

print(f"\n{datetime.now()}")
print(dumps(datetime.now(), default=json_serial))

class Dict(dict):
    def keys_list(self):
        _list = []

        if len(self.values()) > 0:
            for key in self.keys():
                _list.append(key)
                
        return _list

builtins.dict = Dict
# vec = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
vec = dict({
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
)
print(vec)

print(vec.keys_list())
print(vec[(vec.keys_list())[0]])