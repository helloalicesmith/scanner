from server import Server
from client import Client

def main():
    thread = Server()
    thread.start()

    client = Client()
    client.send()

    thread.join()

if __name__ == '__main__':
    main()
