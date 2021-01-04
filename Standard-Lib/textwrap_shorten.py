import textwrap
from textwrap_example import sample_text

dedented_text  = textwrap.dedent(sample_text)
original = textwrap.fill(dedented_text, width=50)

print('Origianl:\n')
print(original)

shortened = textwrap.shorten(original, 100)
shortened_wrapped = textwrap.fill(shortened, width=50)

print('Shortened:\n')
print(shortened)
print(shortened_wrapped)