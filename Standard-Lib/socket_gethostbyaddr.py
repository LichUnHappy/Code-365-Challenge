import socket

hostname, aliases, addresses = socket.gethostbyaddr('127.0.0.1')
print(hostname)
print(aliases)
print(addresses)