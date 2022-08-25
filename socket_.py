import socket


class Socket():
    def __init__(self):
        self.raw_socket = socket.socket(
            socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
        self.raw_socket.bind(('wlan0', 0))
        self.raw_socket.settimeout(4)
