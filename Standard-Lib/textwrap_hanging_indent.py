import textwrap
from textwrap_example import sample_text

detended_text = textwrap.dedent(sample_text).strip()
print(textwrap.fill(detended_text, 
                    # first line indent
                    initial_indent='',
                    # rest line indent
                    subsequent_indent='*' * 4,
                    width=50))