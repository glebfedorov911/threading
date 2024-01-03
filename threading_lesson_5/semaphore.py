import threading
import time
import random

# постепенно

max_connections = 5
pool = threading.BoundedSemaphore(value=max_connections)

def test():
    while True:
        with pool:
            slp = random.randint(1, 5)
            print(f"{threading.currentThread().name} - sleep ({slp})")
            time.sleep(slp)

for i in range(10):
    threading.Thread(target=test, name=f'thr-{i}').start()