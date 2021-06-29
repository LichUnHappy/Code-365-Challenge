import socket
import sys

# create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to the port
server_address = ('localhost', 10000)
print(f"starting up on {server_address[0]} port {server_address[1]}")
sock.bind(server_address)

while True:
    print('waiting to receive message')
    data, address = sock.recvfrom(4096)

    print(f"receive {len(data)} byte from {address}")
    print(f"data -> {data}")

    if data:
        sent = sock.sendto(data, address)
        print(f"sent {sent} byte back to {address}")