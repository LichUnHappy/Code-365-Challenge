import json

data = [{'a': "A", 'b': (2,4), 'c': 3.0}]
print('DATA:', repr(data))

data_string = json.dumps(data)
print('ENCODED:', data_string)

decoded = json.loads(data_string)
print('DECONDED:',decoded)

print('ORIGINAL TYPE:', type(data[0]['b']))
print('DECODED TYPE:', type(decoded[0]['b']))
