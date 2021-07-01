import json

data = [{'a': "A", 'b': (2,4), 'c': 3.0}]
print('DATA:', repr(data))

unsorted = json.dumps(data, sort_keys=False)
print('JSON:', json.dumps(data))
print('SORT:', json.dumps(data, sort_keys=True))

first = json.dumps(data, sort_keys=True)
second = json.dumps(data, sort_keys=True)

print('Unsorted match:', unsorted == first)
print('Sorted match:', first == second)


