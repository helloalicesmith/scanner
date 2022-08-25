import time
import ipaddress

from settings import settings
from utils import get_arp_datagram, get_hardware_hex
from socket_ import Socket


class Client(Socket):
    def __init__(self, net):
        super().__init__()
        self.net = ipaddress.IPv4Network(net)

    def send(self):
        for ip in self.net:
            arp_d = get_arp_datagram(str(ip), get_hardware_hex(settings.mac))
            self.raw_socket.send(arp_d)
            # TODO
            time.sleep(0.03)
