import time
import threading

def get_data(data):
    for _ in range(5):
        print(f"[{threading.current_thread().name}] - {data}")
        time.sleep(1)

thr = threading.Thread(target=get_data, args=(str(time.time()),), daemon=True) # daemon = True -> конец программы = конец потоков
# daemon = False -> конец программы != конец потоков
thr.start()
time.sleep(1)
print('finish')