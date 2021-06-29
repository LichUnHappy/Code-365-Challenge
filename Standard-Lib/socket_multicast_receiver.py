import socket
import sys
import struct

multicast_group = '224.3.29.71'
server_address = ('', 10000)

# create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind to the server address
sock.bind(server_address)

# tell the os to add the socket to the multicast group on all interfaces
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_ADD_MEMBERSHIP,
    mreq
)

while True:
    print("waiting to receive message")
    data, address = sock.recvfrom(1024)

    print(f"receive -> {len(data)} byte from {address} ")
    print(data)

    print(f"sending ack to {address}")
    sock.sendto(b'ack', address)