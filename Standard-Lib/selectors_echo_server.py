import selectors
import socket

mysel = selectors.DefaultSelector()
keep_running = True

def read(connection, mask):
    "callback for read events"
    global keep_running

    client_address = connection.getpeername()
    print(f"read({client_address})")
    data = connection.recv(4096)

    if data:
        # a readable client socket has data
        print(f"received -> {data}")
        connection.sendall(data)
    else:
        # interpret empty result as closed conncetion
        print('closing')
        mysel.unregister(connection)
        connection.close()
        # tell the main loop to stop
        keep_running = False

def accept(sock, mask):
    "callback for new conncetions"
    new_connection, addr = sock.accept()
    print(f"accept -> {addr}")
    new_connection.setblocking(False)
    mysel.register(new_connection, selectors.EVENT_READ, read)

server_address = ('localhost', 10000)
print(f"starting up on {server_address[0]} port {server_address[1]}")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(server_address)
server.listen(5)

mysel.register(server, selectors.EVENT_READ, accept)

while keep_running:
    print("waiting for I/O")
    for key, mask in mysel.select(timeout=1):
        callback = key.data
        callback(key.fileobj, mask)
        # print(mask)
        # print(key)

print('shutting down')
mysel.close()