import socket

HOSTS = [
    'Promethus',
    'google.com',
    'www.python.org.com',
    'nosuchusename',
]

for host in HOSTS:
    try:
        print(f"{host} : {socket.gethostbyname(host)}")
    except socket.error as msg:
        print(f"{host} : {msg}")