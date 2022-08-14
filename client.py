from settings import settings
from utils import get_arp_datagram, get_hardware_hex
from ssocket import Socket

class Client(Socket):
    def send(self):
        destination = f'192.168.0.100'

        arp_d = get_arp_datagram(destination, get_hardware_hex(settings.mac))
        self.raw_socket.send(arp_d)


