import threading
import socketserver

class ThreadedEchoRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # echo the data back to the client
        data = self.request.recv(1024)
        cur_thread = threading.currentThread()
        response = b"%s %s" % (cur_thread.getName().encode(), data)
        self.request.send(response)
        return

class ThreadEchoServer(socketserver.ThreadingMixIn, socketserver.TCPServer):

    pass

if __name__ =="__main__":
    import socket

    address = ('localhost', 0)
    server = ThreadEchoServer(address, ThreadedEchoRequestHandler)

    ip, port = server.server_address

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()
    print(f"server loop running in thread: {t.getName()}")

    # conncet to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # send the data
    message = b'Hello World'
    print(f"sending -> {message}")
    len_sent = s.send(message)
    print(len_sent)

    # receive a response
    response = s.recv(1024)
    print(f"received: {response}")

    # clean up
    server.shutdown()
    s.close()
    server.socket.close()