from settings import settings
from utils import get_arp_datagram, get_hardware_hex
from ssocket import Socket
import time

class Client(Socket):
    def send(self):
         for x in range(2, 150):
            arp_d = get_arp_datagram(f'192.168.0.{x}', get_hardware_hex(settings.mac))
            self.raw_socket.send(arp_d)
            if x % 4 == 0:
                time.sleep(0.035)


