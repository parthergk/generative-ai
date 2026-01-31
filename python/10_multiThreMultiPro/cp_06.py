import threading 
import time 
import multiprocessing 

def cpu_heavy():
    count = 0 
    for i in range(10**8):
        count += i
    print("done")

if(__name__ == "__main__"):    
    start = time.time()

    # tread1 = [ threading.Thread(target=cpu_heavy) for _ in range(2)]
    proc1 = [ multiprocessing.Process(target=cpu_heavy) for _ in range(2)]
    [t.start() for t in proc1]
    [t.join() for t in proc1]

    end = time.time()

    print(f"time taken {end - start:.2f} second")