import socket
import struct
import binascii
import time
import asyncio
import sched
import time
from uuid import getnode as get_mac
from threading import Thread
from functools import partial
from mac_vendor_lookup import MacLookup
import time

from server import Server
from client import client

client()
thread = Server().run()
# thread.start()
# print(thread.is_alive)

#
# print('from recv_socket')
# # old_timeout = s.gettimeout()
# # s.settimeout(5)

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
#
#     time.sleep(1)
#     break

