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

    def bytes_to_mac_vendor(self, bytes):
        hex = binascii.hexlify(bytes).decode('utf-8')
        result = ''

        for x in range(len(hex)):
            result += hex[x]

            if (x + 1) % 2 == 0 and x != len(hex) - 1:
                result += ':'

        return result

    def run(self):
        while True:
            try:
                data = self.raw_socket.recv(42)

                ethernet_header = data[0:14]
                ethernet_detailed = struct.unpack("!6s6s2s", ethernet_header)

                arp_header = data[14:42]
                arp_detailed = struct.unpack("2s2s1s1s2s6s4s6s4s", arp_header)

                mac = self.bytes_to_mac_vendor(arp_detailed[5])
                src_ip = socket.inet_ntoa(arp_detailed[6])
                print(MacLookup().lookup(mac), mac, src_ip)
            except TimeoutError:
                break
