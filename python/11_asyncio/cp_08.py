import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def task1():
    with lock_a:
        print("Task 1 acuired lock a")
        with lock_b:
            print("Task 1 acuired lock b")

def task2():
    with lock_b:
        print("Task 2 acuired lock a")
        with lock_a:
            print("Task 2 acuired lock b")

t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()