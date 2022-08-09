import socket
import struct
import binascii
import os
from uuid import getnode as get_mac

from scanner.settings import settings
from scanner.utils.utils import get_arp_datagram, get_hardware_hex, get_interface_card

interface = get_interface_card()

with socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806)) as s:
    s.bind(('wlan0', 0))

    for i in range(255):
        # TODO 
        destination = f'192.168.0.{i}'

        arp_d = get_arp_datagram(destination, get_hardware_hex(settings.mac))
        s.send(arp_d)


    while True:
        data = s.recv(42)
    
        ethernet_header = data[0:14]
        ethernet_detailed = struct.unpack("!6s6s2s", ethernet_header)
    
        arp_header = data[14:42]
        arp_detailed = struct.unpack("2s2s1s1s2s6s4s6s4s", arp_header)
    
    
        src_ip = socket.inet_ntoa(arp_detailed[6])
        print(socket.inet_ntoa(arp_detailed[6]), socket.inet_ntoa(arp_detailed[8]))

