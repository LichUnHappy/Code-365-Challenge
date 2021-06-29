import binascii
import ipaddress

ADDRESSES = [
    '10.9.0.6',
    'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
]

for ip in ADDRESSES:
    addr = ipaddress.ip_address(ip)
    print(f"{addr}")
    print(f"IP Version:{addr.version}")
    print(f"is private:{addr.is_private}")
    print(f"packed form:{binascii.hexlify(addr.packed)}")
    print(f"integer:{int(addr)}\n")