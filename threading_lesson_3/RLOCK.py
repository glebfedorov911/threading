import threading

locker = threading.RLock() #из любого потока нельзя разблокировать путь для другого

def inc_value():
    print("Block")
    locker.acquire()
    print("Unblock")
    # locker.release()

t1 = threading.Thread(target=inc_value)
t2 = threading.Thread(target=inc_value)

t1.start()
t2.start()