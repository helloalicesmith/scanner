from server import Server
from client import Client

thread = Server()
thread.start()

client = Client()
client.send()

