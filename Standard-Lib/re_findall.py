import re

text = 'abbaaabbbaaa'

pattern = 'ab'

for match in re.findall(pattern, text):
    print('Find {!r}'.format(match))
    print(f'Find {match}')