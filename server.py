import socket
import struct
import threading

class Server(threading.Thread):
    def __init__(self):
        super().__init__()
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
        s.bind(('wlan0', 0))
        s.settimeout(3)
        self.raw_socket = s

    def run(self):
        while True:
            try:
                data = self.raw_socket.recv(42)

                ethernet_header = data[0:14]
                ethernet_detailed = struct.unpack("!6s6s2s", ethernet_header)

                arp_header = data[14:42]
                arp_detailed = struct.unpack("2s2s1s1s2s6s4s6s4s", arp_header)

                print(arp_detailed[5])
                # print(binascii.hexlify(arp_detailed[5]).decode("utf-8"))
                # print(MacLookup().lookup(binascii.hexlify(arp_detailed[5]).decode("utf-8")))

                src_ip = socket.inet_ntoa(arp_detailed[6])
                print(src_ip, socket.inet_ntoa(arp_detailed[8]))
                # s.settimeout(old_timeout) # Restore
            except:
                print('end')
                break
