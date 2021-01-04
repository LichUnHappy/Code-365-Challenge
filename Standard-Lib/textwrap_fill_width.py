import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text).strip()
# print(dedented_text)
for width in [45, 60]:
    print('{} Colums:\n'.format(width))
    print(textwrap.fill(dedented_text, width=width))
    print()