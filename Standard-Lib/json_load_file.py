import io
import json

data = '[{"a": "A", "b": [2, 4], "c": 3.0}]'

f = io.StringIO(data)

print(json.load(f))