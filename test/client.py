import socket
import threading
from all import get, sent

HOST = (socket.gethostname(), 10000)

name = input("Введите имя: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(HOST)

s.send(name.encode())

server_name = s.recv(4096)

print(server_name.decode(), "присоединился")

while True:
    threading.Thread(target=get, args=(s, server_name)).start()
    threading.Thread(target=sent, args=(s, name)).start()