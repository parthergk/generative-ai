
import threading
import time

def boil_milk():
    print(f"Boiling the milk...")
    time.sleep(2)
    print(f"Milk boiled")

def toast_boil():
    print(f"Boiling toast...")
    time.sleep(3)
    print(f"boiled toast")

start = time.time()

thr_1 = threading.Thread(target=boil_milk)
thr_2 = threading.Thread(target=toast_boil)

thr_1.start()
thr_2.start()

thr_1.join()
thr_2.join()

end = time.time()


print(f"total time: {end-start:.2f}")