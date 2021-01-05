import re

text = 'abbaaabbbaaa'

pattern = 'ab'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found {!r} at {:d}:{:d}'.format(text[s:e], s, e))
    print(f"Found {text[s:e]} at {s}:{e}")