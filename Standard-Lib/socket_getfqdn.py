import socket

for host in ['google.com', 'python.com', 'ntu.edu.sg', 'ntulearn.ntu.edu.sg']:
    print(f"{host} : {socket.getfqdn(host)}")