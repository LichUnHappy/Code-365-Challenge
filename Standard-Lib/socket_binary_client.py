import socket
import sys
import struct
import binascii

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.connect(server_address)

values = (1, b'ab', 2.7)
packer = struct.Struct('I 2s f')
packed_data = packer.pack(*values)

print(f"values = {values}")

try:
    # send data
    print(f"sending -> {binascii.hexlify(packed_data)}")
    sock.sendall(packed_data)
finally:
    print("closing socket")
    sock.close()