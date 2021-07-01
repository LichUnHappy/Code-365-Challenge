import io
import json

data = [{'a': "A", 'b': (2,4), 'c': 3.0}]

# 可以緩衝區也可以套接字或文件句柄
f = io.StringIO()
json.dump(data, f)

print(f.getvalue())