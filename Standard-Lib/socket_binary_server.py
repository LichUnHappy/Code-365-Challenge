import socket
import sys
import struct
import binascii

# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.bind(server_address)
sock.listen(1)

unpacker = struct.Struct("I 2s f")

while True:
    print("waiting for a connection")
    conncetion, client_address = sock.accept()

    try:
        data = conncetion.recv(unpacker.size)
        print(f"received -> {binascii.hexlify(data)}")
        print(f"received raw -> {data}")

        unpacked_data = unpacker.unpack(data)
        print(f"unpacked -> {unpacked_data}")
    
    finally:
        conncetion.close()