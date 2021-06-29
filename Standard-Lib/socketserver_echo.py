import logging
import sys
import socketserver

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s : %(message)s'
)

class EchoRequestHandler(socketserver.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        
        self.logger = logging.getLogger('EchoRequestHandler')
        self.logger.debug("__init__")
        socketserver.BaseRequestHandler.__init__(self, request, client_address, server)
        return

    def setup(self):
    
        self.logger.debug('setup')
        return socketserver.BaseRequestHandler.setup(self)

    def handle(self):

        self.logger.debug('handle')

        # echo the data back to the client and append a hello
        data = self.request.recv(1024)
        self.logger.debug(f"recv() -> {data}") 
        return   

    def finish(self):
        
        self.logger.debug('finish')
        return socketserver.BaseRequestHandler.finish(self)

class EchoServer(socketserver.TCPServer):

    def __init__(self, server_address, handler_class=EchoRequestHandler):
        self.logger = logging.getLogger('EchoServer')
        self.logger.debug("__init__")
        socketserver.TCPServer.__init__(self, server_address, handler_class)
        return

    def server_activate(self):
        self.logger.debug('server activate')
        socketserver.TCPServer.server_activate(self)
        return
    
    def server_forever(self, poll_interval=0.5):
        self.logger.debug('waiting for request')
        self.logger.info(
            'handling requests, press <Ctrl-C> to quit'
        )
        socketserver.TCPServer(self, poll_interval)
        return

    def handle_request(self):
        self.logger.debug('handle_request')
        return socketserver.TCPServer.handle_request(self)

    def verify_request(self, request, client_address):
        self.logger.debug(f"verify_request -> {request} -> {client_address}")
        return socketserver.TCPServer.verify_request(self, request, client_address)

    def process_request(self, request, client_address):
        self.logger.debug(f"process_request -> {request} -> {client_address}")
        return socketserver.TCPServer.process_request(self, request, client_address)

    def server_close(self):
        self.logger.debug('server close')
        return socketserver.TCPServer.server_close(self)
    
    def finish_request(self, request, client_address):
        self.logger.debug(f"finish_request -> {request} {client_address}")
        return socketserver.TCPServer.finish_request(self, request, client_address)
    
    def close_request(self, request_address):
        self.logger.debug(f"close_request -> {request_address}")
        return socketserver.TCPServer.close_request(self, request_address)

    def shutdown(self):
        self.logger.debug('shutdown()')
        return socketserver.TCPServer.shutdown(self)

if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 0)
    server = EchoServer(address, EchoRequestHandler)
    ip, port = server.server_address

    # start the server in a thread
    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True) # do not hang on exit
    t.start()

    logger = logging.getLogger('client')
    logger.info(f"server on {ip} port {port}")

    # connect to the server
    logger.debug('creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.debug('connecting to server')
    s.connect((ip, port))

    # send the data
    message = "Hello, world".encode()
    logger.debug(f"sending data -> {message}")
    len_sent = s.send(message)

    # receive a response
    logger.debug('waiting for respond')
    response = s.recv(len_sent)
    logger.debug(f"respond from server: {response}")

    # clean up
    server.shutdown()
    logger.debug('closing socket')
    s.close()
    logger.debug('done')
    server.socket.close()