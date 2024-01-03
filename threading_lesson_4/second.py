import time
import threading

data = threading.local() #хранилище

# def get():
#     print(data.value)
#
# def t1():
#     data.value = 111
#     print(data.value)
#
# def t2():
#     data.value = 222
#     print(data.value)

def t1():
    data.value = {'value': 1}
    print('t1', data.value)

def t2():
    data.test = [1, 2, 3]
    print('t2', data.test)

threading.Thread(target=t1).start()
threading.Thread(target=t2).start()