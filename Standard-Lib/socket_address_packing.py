import socket
import binascii
import struct
import sys

for string_address in ['192.168.1.1', '127.0.0.1']:
    packed = socket.inet_aton(string_address)
    print(f"Original -> {string_address}")
    print(f"packed -> {binascii.hexlify(packed)}")
    print(f" -- {packed}")
    print(f"Unpacked -> {socket.inet_ntoa(packed)}")
    print()