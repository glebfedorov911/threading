import time

def get(conn, name):
    msg = conn.recv(4096)
    print(name.decode(), ":", msg.decode())

def sent(conn, name):
    time.sleep(0.5)
    msg = input("")
    conn.send(msg.encode())
    print(name, ":", msg)
