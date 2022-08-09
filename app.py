import socket
import struct
import binascii
import os
from uuid import getnode as get_mac
from settings import settings
from constants import *

from utils.convert_util import get_hardware_addr

def get_interface_card():
    card = os.listdir('/sys/class/net/')

    for item in card:
        if item[0:2] == 'wl':
            return item

interface = get_interface_card()

gateway_ip = socket.inet_aton("192.168.0.1")
gateway_mac = b"\xff\xff\xff\xff\xff\xff"

mac = get_hardware_addr(settings.mac)

destination_ip = socket.inet_aton("192.168.0.106")
destination_mac = b"\x00\x00\x00\x00\x00\x00"

protocol = htype + ptype + hlen + plen + operation
eth = gateway_mac + mac + arp_code

with socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806)) as s:
    s.bind(('wlan0', 0))

    for i in range(255):
        arp_d = eth + protocol + mac + socket.inet_aton(f"192.168.0.{i}") + destination_mac + destination_ip
        s.send(arp_d)


    # while True:
    #     data = s.recv(42)
    #
    #     ethernet_header = data[0:14]
    #     ethernet_detailed = struct.unpack("!6s6s2s", ethernet_header)
    #
    #     arp_header = data[14:42]
    #     arp_detailed = struct.unpack("2s2s1s1s2s6s4s6s4s", arp_header)
    #
    #
    #     src_ip = socket.inet_ntoa(arp_detailed[6])
    #     print(socket.inet_ntoa(arp_detailed[6]), socket.inet_ntoa(arp_detailed[8]))

