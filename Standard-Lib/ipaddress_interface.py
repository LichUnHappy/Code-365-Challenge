import binascii
import ipaddress

ADDRESSES = [
    '10.9.0.6',
    'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
]

for ip in ADDRESSES:
    iface = ipaddress.ip_interface(ip)
    print(f"iface")
    print(f"network:{iface.network}")
    print(f"ip:{iface.ip}")
    print(f"ip with prefix:{iface.with_prefixlen}")
    print(f"netmask:{iface.with_netmask}")
    print(f"hostmask:{iface.with_hostmask}")
    print()