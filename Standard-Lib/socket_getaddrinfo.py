import socket

def get_constant(prefix):

    return{
        getattr(socket, n): n 
        for n in dir(socket)
        if n.startswith(prefix)
    }

families = get_constant("AF_")
print(families)
print()

types = get_constant("SOCK_")
print(types)
print()

protocols = get_constant("IPPROTO_")
print(protocols)
print()

for respond in socket.getaddrinfo("www.python.org", "http"):

    family, socktype, proto, cannoname, sockaddr = respond



    print(f"Family -> {family} ->{families[family]}")
    print(f"Type -> {socktype} -> {types[socktype]} ")
    print(f"Protocol -> {proto} -> {protocols[proto]}")
    print(f"Canonical name -> {cannoname}")
    print(f"Socket address -> {sockaddr}")
    print()