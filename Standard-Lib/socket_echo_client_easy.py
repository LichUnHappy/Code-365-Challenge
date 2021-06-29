import socket
import sys

def get_constants(prefix):

    return {
        getattr(socket, n): n 
        for n in dir(socket)
        if n.startswith(prefix)
    }

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

# create a TCP/IP socket
sock = socket.create_connection(('localhost', 10000))

print(f"familiy : {families[sock.family]}")
print(f"Type : {types[sock.type]}")
print(f"Protocol ： {protocols[sock.proto]}")
print()

try:

    # send data
    message = b'This is the message. It will be repeated.'
    print(f"sending -> {message}")
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print(f"received -> {data}")

finally:
    print("closing socket")
    sock.close()
