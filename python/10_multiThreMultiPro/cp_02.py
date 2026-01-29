from multiprocessing import Process
import time

def heavy():
    total = 0
    for i in range(10):
        total += i
        print(f"total: {total}")
        time.sleep(2)
    print("done")

if __name__ == '__main__':
    p1 = Process(target=heavy)
    p2 = Process(target=heavy)

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()