import socket

HOSTS = [
    'Promethus',
    'google.com',
    'www.python.org.com',
    'nosuchusename',
]

for host in HOSTS:
    print(host)
    try:
        # print(f"{host} : {socket.gethostbyname(host)}")
        name, aliases, addresses = socket.gethostbyname_ex(host)
        print(f"Hostname : {name}")
        print(f"Aliases : {aliases}")
        print(f"Addresses : {addresses}\n\n")
    except socket.error as msg:
        print(f"{host} : {msg}")