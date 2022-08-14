import socket
import struct
import threading
import binascii
from mac_vendor_lookup import MacLookup

from ssocket import Socket

class Server(threading.Thread, Socket):
    def __init__(self):
        Socket.__init__(self)
        threading.Thread.__init__(self)

    def run(self):
        while True:
            try:
                data = self.raw_socket.recv(42)

                ethernet_header = data[0:14]
                ethernet_detailed = struct.unpack("!6s6s2s", ethernet_header)

                arp_header = data[14:42]
                arp_detailed = struct.unpack("2s2s1s1s2s6s4s6s4s", arp_header)

                print(binascii.hexlify(arp_detailed[5]))
                # print(binascii.hexlify(arp_detailed[5]).decode("utf-8"))
                # print(MacLookup().lookup(binascii.hexlify(arp_detailed[5]).decode("utf-8")))

                src_ip = socket.inet_ntoa(arp_detailed[6])
                print(src_ip, socket.inet_ntoa(arp_detailed[8]))
                # s.settimeout(old_timeout) # Restore
            except ValueError:
                print('end', ValueError)
                break
