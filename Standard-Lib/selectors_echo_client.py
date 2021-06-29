import selectors
import socket

mysel = selectors.DefaultSelector()
keep_running = True
outgoing = [
    b'It will be repeated.', 
    b'This is the message .'
]
bytes_sent = 0
bytes_received = 0

# connecting is a blocking opearation, so call setblocking() to release after it returns
server_address = ('localhost', 10000)
print(f"connecting to {server_address[0]} port {server_address[1]}")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
sock.setblocking(False)

# set up the selector to watch for when the socket is ready to send data as well as when there is data to send
mysel.register(
    sock,
    selectors.EVENT_READ | selectors.EVENT_WRITE,
)

while keep_running:
    print("waiting for I/O")
    for key, mask in mysel.select(timeout=1):
        connection = key.fileobj
        client_address = connection.getpeername()
        print(f"client -> {client_address}")

        if mask & selectors.EVENT_READ:
            print("ready to read")
            data = connection.recv(1024)
            if data:
                # a readable client socket has data
                print(f"received -> {data}")
                bytes_received += len(data)

            # interpret empty result as closed connection and also close when received a copy of all of the data sent
            keep_running = not (
                data or 
                (
                    bytes_received and (
                        bytes_received == bytes_sent
                    )
                )
            )
        
        if mask & selectors.EVENT_WRITE:
            print("ready to write")
            if not outgoing:
                # out of message, so no longer need to write anything. change the registration to keep reading respond from the server
                print('switching to read-only')
                mysel.modify(sock, selectors.EVENT_READ)
            else:
                # send the next message
                next_msg = outgoing.pop()
                print(f"sending {next_msg}")
                sock.sendall(next_msg)
                bytes_sent += len(next_msg)

print("shutting down")
mysel.unregister(connection)
connection.close()