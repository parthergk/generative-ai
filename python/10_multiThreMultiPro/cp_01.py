import threading
import time 

def geting():
    for i in range(5):
        print(f"geting the item {i}")
        time.sleep(2)

def procin():
    for i in range(5):
        print(f"procin the item {i}")
        time.sleep(3)

get_thr = threading.Thread(target=geting)
pro_thr = threading.Thread(target=procin)

get_thr.start()
pro_thr.start()

get_thr.join()
pro_thr.join()