import os
import socketserver

class ForkingEchoRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # echo the data back to the client
        data = self.request.recv(1024)
        cur_pid = os.getpgid()
        response = b'%d: %s' % (cur_pid, data)
        self.request.send(response)
        return

class ForkingEchoServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    
    pass

if __name__ == "__main__":
    import socket
    import threading

    address = ('localhost', 0)
    server = ForkingEchoServer(address, ForkingEchoRequestHandler)
    ip, port = server.server_address

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()
    print(f"server loop running in process: {t.getName()}")

    # coonect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # send the data
    message = 'Hello world'.encode()
    print(f"sending : {message}")
    len_sent = s.send(message)

    # receive a response
    response = s.recv(1024)
    print(f"received: {response}")

    # clean up
    server.shutdown()
    s.close()
    server.socket.close()