import socket
import sys

# create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = b'This is the message. It will be repeated.'

try:

    # send data
    print(f"sending -> {message}")
    sent = sock.sendto(message, server_address)

    # receive respond
    print("waiting to receive")
    data, server = sock.recvfrom(4096)
    print(f"received respond -> {data}")

finally:
    print("close the socket")
    sock.close()