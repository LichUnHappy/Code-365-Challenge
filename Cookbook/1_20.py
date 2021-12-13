# 合并多个字典或映射
# chainmap

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap

c = ChainMap(b, a)

for k, v in c.items():
    print(k, v)