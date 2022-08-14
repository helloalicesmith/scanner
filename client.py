import socket
import time

from settings import settings

from utils import get_arp_datagram, get_hardware_hex

def client():
    with socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806)) as s:
        s.bind(('wlan0', 0))

        time.sleep(2)

        print("main")
        destination = f'192.168.0.100'

        arp_d = get_arp_datagram(destination, get_hardware_hex(settings.mac))
        s.send(arp_d)
