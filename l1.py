import threading
import time

def get_data(val):
    while 1:
        print(val)
        time.sleep(1)

def get_data_2(val):
    for i in range(val):
        print('123')
        time.sleep(1)

thr = threading.Thread(target=get_data, args=(time.time(), ))
thr2 = threading.Thread(target=get_data_2, args=(12, ))
thr.start()
thr2.start()

thr2.join()

i = input("Hello, u name?: ")
print(i)