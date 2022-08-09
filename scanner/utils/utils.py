import socket
import os

from ..constants import *

def get_hardware_hex(hex: str):
    return hex.replace(':', '')

def get_arp_datagram(destination_ip: str, hardware_hex: str):
    hardware_addr = bytes.fromhex(hardware_hex)
    arp_header = htype + ptype + hlen + plen + operation
    destination_mac = b"\x00\x00\x00\x00\x00\x00"
    broadcast_mac = b"\xff\xff\xff\xff\xff\xff"

    eth = broadcast_mac + hardware_addr + arp_code

    arp_datagram = eth + arp_header + hardware_addr + socket.inet_aton(socket.gethostbyname(socket.gethostname())) + destination_mac + socket.inet_aton(destination_ip)

    return arp_datagram

def get_interface_card():
    card = os.listdir('/sys/class/net/')

    for item in card:
        if item[0:2] == 'wl':
            return item

