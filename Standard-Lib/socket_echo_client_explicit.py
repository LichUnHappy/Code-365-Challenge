import socket
import sys

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conncet the socket to the port on the server
# given by the caller
server_address = (sys.argv[1], 10000)
print(f"connecting to {server_address[0]} port {server_address[1]}")
sock.connect(server_address)

try:
    # send data
    message = b'This is the message. It will be repeated.'
    print(f"sending -> {message}")
    sock.sendall(message)

    # look for the respond
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(80)
        amount_received += len(data)
        print(f"received -> {data}")
finally:
    print("closing socket")
    sock.close()
