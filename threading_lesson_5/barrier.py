import time
import random
import threading

# все и сразу

def test(barrier: threading.Barrier):
    slp = random.randint(3, 7)
    print(f"Поток [{threading.currentThread().name}] запущен в ({time.ctime()})")
    time.sleep(slp)

    barrier.wait()
    print(f"Поток [{threading.currentThread().name}] преодолел барьер в ({time.ctime()})")

bar = threading.Barrier(5)
for i in range(5):
    threading.Thread(target=test, args=(bar, ), name=f"thr-{i}").start()