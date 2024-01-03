import time
import threading

value = 0
locker = threading.Lock() #из любого потока можно разблокировать путь для другого

def inc_value():
    global value
    while True:
        with locker:
            value += 1
            time.sleep(1)
            print(value, threading.currentThread().name)

def second_inc_value():
    print("Блокируем поток...")
    locker.acquire()
    print("Поток разблокирован...")
    # locker.release()

# for i in range(5):
#     threading.Thread(target=inc_value, name=f"potok {i}").start()

t1 = threading.Thread(target=second_inc_value)
t2 = threading.Thread(target=second_inc_value)

t1.start()
t2.start()