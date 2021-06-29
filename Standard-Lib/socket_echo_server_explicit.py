import socket
import sys

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the address given
server_name = sys.argv[1]
# print(f"receive parar list {server_name}")
server_address = (server_name, 10000)
print(f"starting up on {server_address[0]} port {server_address[1]}")
sock.bind(server_address)
sock.listen(1)

while True:
    # wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    try:
        print(f"conncetion from {client_address}")

        # receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print(f"receive -> {data}")
            if data:
                print("sending data back to the client")
                connection.sendall(data)
            else:
                print(f"no data from {client_address}")
                break
    finally:
        # clean up the conncetion
        connection.close()