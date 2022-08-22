import sys
from mac_vendor_lookup import MacLookup

from server import Server
from client import Client

#TODO
def main(argv):
    # MacLookup().update_vendors()
    server = Server()
    server.start()

    client = Client()
    client.send()

    server.join()

    print(server.result)

if __name__ == '__main__':
    main(sys.argv)
