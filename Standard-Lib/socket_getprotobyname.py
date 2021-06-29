import socket 

def get_constant(prefix):

    return {
        getattr(socket, n): n for n in dir(socket) if n.startswith(prefix)
    }

protocols = get_constant("IPPROTO_")
print(protocols)

for name in ['icmp', 'udp', 'tcp']:
    proto_num = socket.getprotobyname(name)
    const_name = protocols[proto_num]
    print(f"{name} - {proto_num} - {const_name} - {getattr(socket, const_name)}")