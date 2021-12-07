from collections import OrderedDict

d = OrderedDict()
d['cat'] = 1
d['dog'] = 2
d['lion'] = 3
d['bat'] = 4

for key in d:
    print(key, d[key])

import json
print(json.dumps(d))

