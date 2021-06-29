import ipaddress

NETWORKS = [
    '10.9.0.0/24',
    'fdfd:87b5:b475:5e3e::/64',
]

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print(f"{net}")
    print(f"broadcast:{net.broadcast_address}")
    print(f"is private:{net.is_private}")
    print(f"compressed:{net.compressed}")
    print(f"with netmask:{net.with_netmask}")
    print(f"with hostname:{net.with_hostmask}")
    print(f"num addresses:{net.num_addresses}\n\n")

