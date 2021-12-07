# 删除序列相同元素并保持顺序

# hashable element
def dedupe(items):
    memo = set()
    for item in items:
        if item not in memo:
            yield item
            memo.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))

# unhashable element
def dedupe(items, key=None):
    memo = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in memo:
            yield val
            memo.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))
print(list(dedupe(a, key=lambda d: d['x'])))