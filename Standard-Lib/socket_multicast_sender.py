import socket
import sys
import struct

message = b'very important data'
multicast_group = ('224.3.29.71', 10000)

# create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# set a timeout so the socket does not block
# indefinitely when trying to receive data
sock.settimeout(0.2)

# set the time-to-live for message to 1 so they do not go past the local network segement
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:

    # send data to the multicast group
    print(f"sending -> {message}")
    sent = sock.sendto(message, multicast_group)

    # lool for respond from all recipients
    while True:
        print("waiting to receive")
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print("time out, no more respond")
            break
        else:
            print(f"receive -> {data} from -> {server} ")
finally:
    print("close socket")
    sock.close()