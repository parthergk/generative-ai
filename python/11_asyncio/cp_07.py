import threading
import time 

def monitor_fun():
    while True:
        print(f"Monitoring fun....")
        time.sleep(2)

t = threading.Thread(target=monitor_fun, daemon=True)

t.start()

print("main thread")