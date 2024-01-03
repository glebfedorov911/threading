import socket
from all import get, sent
import threading

HOST = (socket.gethostname(), 10000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(HOST)
s.listen()

name = input('Введите имя: ')
conn, addr = s.accept()

name_user = conn.recv(4096)
print(name_user.decode(), 'присоединился')

conn.send(name.encode())

print("START")

while True:
    threading.Thread(target=get, args=(conn, name_user)).start()
    threading.Thread(target=sent, args=(conn, name)).start()