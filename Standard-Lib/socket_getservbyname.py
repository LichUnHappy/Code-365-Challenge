import socket 
from urllib.parse import urlparse

URLS = [
    'https://www.python.org',
    'https://www.mybank.com',
    'ftp://prep.ai.mit.edu',
    # 'gohpher://gopher.micro.umn.edu',
    # 'smtp://mail',
    # '',
    # '',
    # '',
]

for url in URLS:
    parsed_url = urlparse(url)
    print(parsed_url)
    port = socket.getservbyname(parsed_url.scheme)