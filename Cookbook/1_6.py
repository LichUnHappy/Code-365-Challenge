# 字典中的键映射多个值
# multidict

from collections import defaultdict

d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
print(d)

d = defaultdict(set)
d['b'].add(1)
d['b'].add(1)
d['b'].add(2)
print(d)

d = {} # 一个普通的字典
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)